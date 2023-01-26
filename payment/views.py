from django.shortcuts import render
import logging
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException
import logging
from django.http import HttpResponse, Http404

from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from main.models import User_Order, Content, Main_User
def go_to_gateway_view(request):
    user_order = User_Order.objects.get(username=request.user)
    order = Content.objects.get(id=user_order.order)
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = order.price
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989112221234'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create() # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway')
        bank.set_mobile_number(user_mobile_number)  # اختیاری
    
        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید. 
        bank_record = bank.ready()
        
        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e


def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    # در این قسمت باید از طریق داده هایی که در بانک رکورد وجود دارد، رکورد متناظر یا هر اقدام مقتضی دیگر را انجام دهیم
    if bank_record.is_success:
        # پرداخت با موفقیت انجام پذیرفته است و بانک تایید کرده است.
        # می توانید کاربر را به صفحه نتیجه هدایت کنید یا نتیجه را نمایش دهید.
        #return HttpResponse("پرداخت با موفقیت انجام شد.")
        user_order = User_Order.objects.get(username=request.user)
        content = Content.publish.get(id=user_order.order)
        try:
            Main_User.objects.get(username=request.user)
        except Main_User.DoesNotExist:
            main_user = Main_User(username=request.user)
            main_user.save()
        main_user = Main_User.objects.get(username=request.user)
        main_user.bought.add(content)
        return render(request, "main/edu_course.html", {
            "content": content
        })
    # پرداخت موفق نبوده است. اگر پول کم شده است ظرف مدت 72 ساعت پول به حساب شما بازخواهد گشت.
    return HttpResponse("پرداخت با شکست مواجه شده است. اگر پول کم شده است ظرف مدت 72 ساعت پول به حساب شما بازخواهد گشت.")