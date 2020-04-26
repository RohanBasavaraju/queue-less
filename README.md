# QLess
QLess is a mobile application bringing you the shortest wait times for local restaurants, supermarkets, food banks, and more.

This project will be submitted for Cal Hacks 2020 to serve as a platform helping those afflicted by the COVID-19 pandemic.

# Inspiration

Our team was inspired to build QLess in light of the devastating conditions imposed by the global COVID-19 pandemic. While nearly every aspect of our lives has been afflicted, there is one constant that plagues our health and our happiness: food. Access to a steady food source, whether it be from restaurants, supermarkets, or food banks, has been taken for granted in modern society. As the coronavirus extends its reach around the world, food providers have been faced with the challenge of balancing food inventory and recurring revenue with the social distancing of both customers and workers. As individuals with first-hand experience of these problems, we knew there had to be a better way of meeting our dietary and (anti-)social needs. Enter: QLess.

# What it does

QLess is a mobile application that provides members of a community with real-time analytics on wait times at local food markets. QLess scales to a diverse userbase by customizing its insights for individuals regardless of their social and economic backgrounds. This provides users with up-to-date info on the queue length of local food suppliers from high-end eateries to government-funded food stamps. The quantity and quality of partnerships with nearby food facilities will also be expanded upon through partnerships with relevant organizations (see "What's next for QLess" below). Our current offerings include locating local food suppliers and sorting search results by distance and queue waiting time.

# How I built it

On the front-end, ... .

On the back-end, the QLess team created a relation database using Python, SQL, and Google Cloud to maintain real-time access to local food suppliers and the foot traffic they experience throughout the day. We also built multiple RESTful APIs using Java and Dart to enable efficient database access and storage. To meet user needs, we developed a suite of utility functions using Google Maps and its Geolocation API that will connect users with personalized results in seconds. These functionalities include: detecting geographic location of the mobile device, searching nearby stores using user input, computing relative distance between the user and food-bearing facilities, and providing local recommendations optimized for time and safety.

# Challenges I ran into

# Accomplishments that I'm proud of

# What I learned

# What's next for QLess

After our initial proof of concept, QLess aspires to revolutionize the food analytics industry through five major avenues.

First, QLess will make its services more accessible to communities around the world by partnering with more diverse businesses, governmental organizations, and nonprofits in the food sector. This will provide our users with a greater variety of choices for meeting nutritional needs, especially in highly populated regions with increased risk of contracting COVID-19.

Second, QLess seeks to create a food inventory management system to track food supply that is readily available on shelves and in back storage along with using predictive analytics to determine when the next shipment of product will be accessible to food suppliers.

Third, QLess aims to optimize the user experience by allowing consumers to filter food locations by operating hours, customer feedback, coupons, discounts, etc. This would expand our current setup which simply filters for queue time and relative distance.

Fourth, QLess plans to further personalize the user interface by employing artificial intelligence (AI) to better understand user preferences and dietary restrictions in conjunction with their present nutritional needs. This serves as a supplement to users by assisting them in determining which food products to purchase while minimizing time spent at the shop while obeying social distancing best practices. Additionally, we can use targeted machine learning by saving details from your positively-reviewed locations and making recommendations to potential top picks for your next shopping spree.

Lastly, QLess looks to improve customer engagement by making the service digitally accessible to those in highly populated regions around the world. As such, we seek to expand our platform across Android, iOS, and web devices. We are currently prototyping our technology on the Android platform with the intent of product launch to users globally in the coming weeks. From here we can optimize our future endeavors on the iOS and web platforms for a comprehensive foodie experience.
