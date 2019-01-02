import webbrowser
import pyperclip,sys

# w = webbrowser.open("http://inventwithpython.com/")

# print(w)  # Boolean Type (True even if webpage does not exists)

if len(sys.argv)<2:
    clip = pyperclip.paste()
    # Newclip = clip
    # while clip==Newclip:      # infinite check of changing clipboard
    #     clip = pyperclip.paste()
    #870 Valencia St, San Francisco, CA 94110
    webbrowser.open("https://www.google.com/maps/place/" + clip)
    # webbrowser.open_new_tab("https://www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8")

else:
    clip = " ".join(sys.argv[1:])
    webbrowser.open("https://www.google.com/maps/place/" + clip)
    # webbrowser.open_new_tab("https://www.google.com/maps/place/870+Valencia+St/@37.7590311,-122.4215096,17z/data=!3m1!4b1!4m2!3m1!1s0x808f7e3dadc07a37:0xc86b0b2bb93b73d8")
