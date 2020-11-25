def perfometer_check_mk_omni_zpool(row, check_command, perf_data):
    left = float(perf_data[0][1])
    warn = float(perf_data[0][3])
    crit = float(perf_data[0][4])
    if left > crit:
        color = "#ff0000"
    elif left > warn:
        color = "#ffff00"
    else:
        color = "#00ff00"

    return "%.0f%%" % left, perfometer_linear(left, color)

perfometers["check_mk-omni_zpool"] = perfometer_check_mk_omni_zpool

# end