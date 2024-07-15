def createYoutubeVideo(title,description):
    video = {"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":"","comment_text":""}}
    return video

def likeAVideo(dict):
    if "likes" in dict:
        dict["likes"] +=1
    return dict

def dislikeAVideo(dict):
    if "dislikes" in dict:
        dict["dislikes"] +=1
    return dict

def addAComment(youtubeVideo,username,commentText):
    youtubeVideo["comments"][username] = commentText
    return 

vid = createYoutubeVideo("CS is the best we are better then the rest ahoo ahoo ahoo ahoo ahoo","cs for life!")
print("Title:",vid["title"])
print("Description:",vid["description"])
print("\n",vid["likes"],"people liked this :)")
print(vid["dislikes"],"people disliked this :(")
print("Comments:")
print(vid["comments"]["username"],":", vid["comments"]["comment_text"])