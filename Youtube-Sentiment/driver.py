import comment_extract as CE
import sentimentYouTube as SYT

def main():
	userpositive = open("userpositive.txt", "w")
	userpositive.write("")
	userpositive.close()
	usernegative = open("usernegative.txt", "w")
	usernegative.write("")
	usernegative.close()
	# EXAMPLE VideoId = 'tCXGJQYZ9JA'
	videoId = input("Enter VideoId : ")
	# Fetch the number of comments
	# if count = -1, fetch all comments
	count = int(input("Enter no. of comments to extract : "))
	comments = CE.commentExtract(videoId, count)
	SYT.sentiment(comments)


if __name__ == '__main__':
	main()
