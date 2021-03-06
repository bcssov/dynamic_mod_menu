from templates.utils import settings, templater

template = """
country_event = {{
    id = dmm_mod_clear_utilities.{count}
    hide_window = yes
    is_triggered_only = yes

    trigger = {{
        has_global_flag = dmm_mod_utilities_{count}
    }}

    immediate = {{                
        remove_global_flag = dmm_mod_utilities_{count}      
        remove_global_flag = dmm_mod_utilities_{count}_disabled   
    }}    
}}"""


def process(publish_dir):
    mod_lines = []
    for i in range(1, settings.total + 1):
        mod_lines.append(template.format(count=i))
    templater.process_file(
        publish_dir + "/events/dmm_mod_clear_utilities.txt", events=mod_lines)
