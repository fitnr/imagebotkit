# image bot kit

Create a bot that post images (and video) to Twitter.

````bash
# Update Twitter with 'image.png'
imagebot screen_name image.png --status "Hello World!"

# Update Twitter with a random image from 'folder/with/images'
imagebot screen_name folder/with/images --status "Hello World!"

# Post a random image, using 'record.txt' as a list of previously-posted images
imagebot screen_name folder/with/images --status "Hello World!" --record record.txt
````

