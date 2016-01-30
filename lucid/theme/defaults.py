from mezzanine.conf import register_setting

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("SOCIAL_LINK_FACEBOOK",
             "SOCIAL_LINK_TWITTER",
             "SOCIAL_LINK_PINTEREST",
             "SOCIAL_LINK_VIMEO",
             "SOCIAL_LINK_TUMBLR",
             "SOCIAL_LINK_DELICIOUS",
             ),
)

register_setting(
    name="SOCIAL_LINK_FACEBOOK",
    label="Facebook link",
    description="If present a Facebook icon linking here will be in the header.",
    editable=True,
    default="https://facebook.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TWITTER",
    label="Twitter link",
    description="If present a Twitter icon linking here will be in the header.",
    editable=True,
    default="https://twitter.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_PINTEREST",
    label="Pinterest link",
    description="If present a Pinterest icon linking here will be in the header.",
    editable=True,
    default="https://pinterest.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_VIMEO",
    label="Vimeo link",
    description="If present a Vimeo icon linking here will be in the header.",
    editable=True,
    default="https://vimeo.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_TUMBLR",
    label="Tumblr link",
    description="If present a Tumblr icon linking here will be in the header.",
    editable=True,
    default="https://tumblr.com/mezzatheme",
)

register_setting(
    name="SOCIAL_LINK_DELICIOUS",
    label="Delicious link",
    description="If present a Delicious icon linking here will be in the header.",
    editable=True,
    default="https://delicious.com/mezzatheme",
)