import discord
from discord.ext import commands


journeyEmbed = discord.Embed(
	title = "Details for your next journey",
	description = "Distance: 2.3mi",
	color = 0x93CEBA
)
journeyEmbed.add_field(
	name = "β° Time",
	value = "```08:20-08:45 (0h25m)```",
	inline = False
)
journeyEmbed.add_field(
	name = "πΆββοΈ Directions ",
	value = """```1. πΆββοΈ Walk 5 mins to Brook Green (Stop H), across the street from St. Paul\'s Hotel 
2. π 13 mins bus ride (9 or 23) to Royal Albert Hall (Stop RL)
3. πΆββοΈ Walk 7 mins to Imperial College EEE Building via Kensington Gore and Exhibition Road ```
""",
	inline = False
)
journeyEmbed.add_field(
	name = "π° Fare",
	value = """```Β£1.5```""",
	inline = False
)
journeyEmbed.add_field(
	name = "π‘ Weather",
	value = """```Wear a raincoat π§```""",
	inline = False
)
journeyEmbed.add_field(
	name = "π¦ Chance of delay",
	value = """```Expect no more than a 0h10m delay at High Street Kensington.```""",
	inline = False
)
journeyEmbed.set_footer(
	text = "from Thyme"
)
journeyEmbed.set_author(
	name = "Requested by this nosy guy "
)
journeyEmbed.set_image(
	url = 'https://raw.githubusercontent.com/cluelesselectrostar/Horizons/master/images/journey_map.png'
)

# Detailed Journey
detailedEmbed = discord.Embed(
	title = "Detailed Directions",
	description = "2.3mi",
	color = 0x93CEBA
)
detailedEmbed.add_field(
	name = "1οΈβ£ Walk To Brook Green Bus Stop (Stop H) πΆββοΈ (0h4m, 0.2mi)",
	value = """```1. Head southeast on Brook Green
2. Turn right on Hammersmith Road (A315), across the street from St. Pauls Hotel```""",
	inline = False
)
detailedEmbed.add_field(
	name = "2οΈβ£ Bus 9 towards Aldwych or 23 towards Westbourne Park π (0h13m, 1.9mi)",
	value = """```Brook Green (Stop H) βοΈ
...
Kensington Palace (Stop M)
Palace Gate (Stop RH)
Queens Gate (Stop RK) 
Royal Albert Hall (Stop RL) βοΈ
 ```
""",
	inline = False
)
detailedEmbed.add_field(
	name = "3οΈβ£ Walk To Imperial College EEE Building πΆββοΈ (0h9m, 0.5mi) ",
	value = """```
1. Head west on Kensington Rd/Kensington Gore/A315
2. Turn left onto Kensington Gore
3. Turn left onto Prince Consort Rd
4. Slight right to stay on Prince Consort Rd
5. At the roundabout, take the 1st exit onto Exhibition Rd
6. Turn right onto Imperial College Rd
7. Turn right onto Unwin Rd
8. Unwin Rd turns left and becomes Ayrton Rd
Destination will be on the right
```""",
	inline = False
)
detailedEmbed.set_footer(
	text = "from Thyme"
)
detailedEmbed.set_author(
	name = "Requested by this nosy guy "
)



home = """

**Welcome home. It's thyme to grab your time back!**

To perform the actions below, react to a button.

β­ Details for your next journey
π Your summary for the day

π‘ Create a new event 
π  Notification Settings

πͺ Perform initial setup (again)

βΉ Exit Thyme
"""

tmrschedule = """

10mins+ commute  to be made on this day:
(1) 08:20-08:45 Brook Green to Imperial College
(2) 18:00-18:25 Imperial College to Brook Green

Anything else?
β­ Details for your next journey

π‘ Create an event
π  Modify or delete an event

π  Thyme Home
βΉ Exit Thyme.
"""

link = """
You can save a lot more thyme if you link me with your calendar and reminder lists. 

Which calendar or list would you like me to link with?
π Your Imperial College calendar
π Your personal calendar
π‘ Create an event manually

π  Thyme Home
βΉ Exit Thyme
"""

linked = """

Hooray! You have successfully linked your calendar to Thyme! π

How would you like me to notify you?
π Active notifications (Phone calls plus texts)
π¬ Semi-active notifications (Text messages)
π² Passive notifications (App notifications and banners) 
π΅ No notifications
"""

requestmanual = """

Enter your event date/time, name and place, each surrounded with "double quotation marks" and seperated with a space. π‘
"""

deletedone = """

Your event has been deleted. π? 

Anything else?
π  Thyme Home
βΉ Exit Thyme
"""

notifications = """

You are now in notification preferences. 
How would you like me to notify you?
π Active notifications (Phone calls plus texts)
π¬ Semi-active notifications (Text messages)
π² Passive notifications (App notifications and banners)
π΅ No notifications

π  Thyme Home
βΉ Exit Thyme
"""

time_interval = """

Your notifications has been updated.

When would you like me to call you in advance of your departure?
1οΈβ£ 5 minutes
2οΈβ£ 30 minutes
3οΈβ£ 1 hour.
4οΈβ£ All of the above.

π  Thyme Home
βΉ Exit Thyme
"""

settings_updated = """

Notification settings updated βοΈ 

π  Thyme Home
βΉ Exit Thyme
"""

requestmodify = """
Enter the number of the event you would like to modify. βοΈ
"""

modifyerror = """
You have input an incorrect number.

How would you like to proceed?
β­ Details for your next journe.
π  Modify or delete an event

π  Thyme Home
βΉ Exit Thyme
"""

modifyoptions = """
What would you like to modify the event?

β± Modify event time
π Modify event name
π Modify event location
πΊ Modify event directions
π Delete event

π  Thyme Home
βΉ Exit Thyme
"""

modifylimit = """
Sorry, you cannot modify an event right now π. You can however delete an event and create a new one. Hopefully this will be implemented sometime later!

π  Thyme Home
βΉ Exit Thyme
"""

anything_else = """
Anything else?
π  Thyme Home
βΉ Exit Thyme
"""

requestdetail = """
Anything else?
π Detailed journey directions

π  Thyme Home
βΉ Exit Thyme
"""




