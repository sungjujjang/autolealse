import getshortlist
import getfiles
import upload
import youtubedownload

base = str(input("쇼츠를 수집할 처음 영상의 링크를 주세요!(알고리즘에 영항이 감) : "))
gesu = int(input("쇼츠를 몇개 수집할까요? : "))
id = str(input("유튜브 채널의 아이디를 주세요! : "))
pw = str(input("유튜브 채널의 비밀번호를 주세요! : "))
videopath = "videos"

paths = r"C:\Users\User\Desktop\workspace\autolelse\videos"

shortlist = getshortlist.get_list(gesu, base)
print(shortlist)
for short in shortlist:
    try:
        print(youtubedownload.downloadYouTube(short, videopath))
    except Exception as e:
        print(e)

files = getfiles.getfiles(paths)
upload.upload(files, id, pw)
print("compleate")