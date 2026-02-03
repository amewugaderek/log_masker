import re
from django.shortcuts import render


def mask_log_payload(payload:str) -> str:
    
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    device_pattern = r'(?<=devname=")[^"]+|(?<=Computer=)[^\s]+|(?<=DeviceName=)[^\s]+'
    
    masked = re.sub(ip_pattern, "XXX.XXX.XXX.XXX", payload)
    masked = re.sub(device_pattern, "DEVICE_NAME_REDACTED", masked)
    
    return masked
   
    
def log_masker_view(request):
    original_log = ""
    masked_log = ""

    if request.method == "POST":
        original_log = request.POST.get("log_input", "")
        if original_log:
            masked_log = mask_log_payload(original_log)

    return render(request, "masker.html", {
        "original_log": original_log,
        "masked_log": masked_log
    })