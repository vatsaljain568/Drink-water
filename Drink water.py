import pync
import time
while True:
    pync.notify(
        title = "**Please drink water by -VATSAL JAIN",
        message = "The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men.",
        app_icon = "icon.png",
        timeout = 3
    )
    time.sleep(3)