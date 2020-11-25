def perfometer_check_mk_omni_smart(row, check_command, perf_data):
    left = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    if left > crit:
        color = "#ff0000"
    elif left > warn:
        color = "#ffff00"
    else:
        color = "#00ff00"

    return "%.0fC" % left, perfometer_linear(left, color)

perfometers["check_mk-omni_smart"] = perfometer_check_mk_omni_smart

# end