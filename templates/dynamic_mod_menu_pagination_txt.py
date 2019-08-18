from templates.utils import settings, templater

template = """
            if = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_processed
                        value = {0}
                    }}
                }}
                switch = {{
                    trigger = has_global_flag

                    {1}
                }}
            }}"""
template_else = """
            else_if = {{
                limit = {{
                    check_variable = {{
                        which = dynamic_mod_menu_items_processed
                        value = {0}
                    }}
                }}
                switch = {{
                    trigger = has_global_flag

                    {1}
                }}
            }}"""
template_mod = """
                    dmm_mod_{1} = {{
                        change_variable = {{
                            which = dynamic_mod_menu_items_shown
                            value = 1
                        }}
                        set_global_flag = dmm_mod_id_{0}_{1}
                    }}"""
template_remove_flag = """
        remove_global_flag = dmm_mod_id_{0}_{1}"""


def process(publish_dir):
    event_1_mod_lines = []
    event_2_mod_lines = []
    event_3_mod_lines = []
    for i in range(1, settings.total + 1):
        mod_text = ""
        for j in range(i, settings.total + 1):
            mod_text += template_mod.format(i, j)
            event_3_mod_lines.append(template_remove_flag.format(i, j))
        if (i == 1):
            event_1_mod_lines.append(template.format(i, mod_text))
        else:
            event_1_mod_lines.append(template_else.format(i, mod_text))

    for i in range(settings.total, 0, -1):
        mod_text = ""
        for j in range(settings.total, i - 1, -1):
            mod_text += template_mod.format(i, j)            
        if (i == settings.total):
            event_2_mod_lines.append(template.format(i, mod_text))
        else:
            event_2_mod_lines.append(template_else.format(i, mod_text))

    templater.process_file(
        publish_dir + "/events/dynamic_mod_menu_pagination.txt",
        event_1_mod_lines,
        event_2_mod_lines,
        event_3_mod_lines)
