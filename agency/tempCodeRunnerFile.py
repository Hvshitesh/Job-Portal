    url(r"^$", index, name="index"),
    url(r"^out/$", getout, name="getout"),
    url(r"^thank-you-message/$", registration_success, name="registration_success"),
    url(r"^how-it-works/$", how_it_works, name="how_it_works"),
    url(r"^dashboard/$", dashboard, name="dashboard"),
    url(r"^mobile/verify/$", verify_mobile, name="verify_mobile"),
    url(
        r"^send/mobile_verification_code/$",
        send_mobile_verification_code,
        name="send_mobile_verification_code",
    ),