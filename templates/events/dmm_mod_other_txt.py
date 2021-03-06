from templates.utils import settings, templater

template = """
country_event = {{
    id = dmm_mod_other.{count}
    title = "dmm_mod_other.{count}.title"
    desc = "dmm_mod_other.{count}.desc"
    picture = GFX_evt_psionics
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod_other_{count}
    }}

    after = {{
        remove_global_flag = dmm_mod_other_{count}_opened
        # Uninstall mod, should be overwritten by an actual mod
        set_global_flag = dmm_mod_other_{count}_disabled
        country_event = {{
            id = dmm_mod_clear_other.{count}
            days = 2
        }}   
    }}

    option = {{        
        name = "dmm_options.close"
    }}
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/events/dmm_mod_other.txt", events=mod_lines)
