def using_control_once():
    if True and True:
        return "Success #1"

def using_control_again():
    if not False:
        return "Success #2"

print using_control_once()
print using_control_again()
