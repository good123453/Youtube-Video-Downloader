# module usage block: use to download social media platform videos and audios
import yt_dlp
import os
import subprocess

# Creator good123453/Neo
# Creator roles: Project Lead & Developer
# Code Architect
# Main Programmer
# Tester & Debugger
# Documentation Writer

# Ai Creator : AI deepseek v3.2 model machine
# deepseek v3.2 model roles: Technical Advisor
# Code Reviewer
# Error Analyst
# Solution Consultant
# Learning Guide




class YoutubeDownloader:
    
    
    # main head boss block: takes list of urls and quality options
    def __init__(self, urls =None , quality = "") -> None:
        
        if urls is None:
            self.urls = []
            print("No url provided")
            
        else:
            self.urls = urls if isinstance(urls, list) else [urls]
            
        self.quality = quality
        self.ydl_object = None
        
        
        

    # setup downloading system block: take quality and decide what to do and set the format otherwise hd format apply
    def setup_downloader(self, ffmpeg_available: bool) -> None:
        
        
        
        
        # computer descision block: if user select sd then computer format low quality otherwise high quality
        if self.quality == "sd": 
            
            # SD quality system block: get best quality up to 480p for SD
            format_str = "best[height<=480][ext=mp4]/worst[ext=mp4]"
            print("✓ SD quality selected (up to 480p)")
            
        else:  # hd
            
            
            
            # HD quality system block: check ffmpeg availability for high quality
            if ffmpeg_available:
                
                
                # FFmpeg available system block: can merge video+audio for 1080p+
                format_str = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
                print("✓ HD quality selected (up to 1080p with FFmpeg)")
            else:
                
                
                # FFmpeg not available system block: use single stream up to 720p
                format_str = "best[height<=720][ext=mp4]/best[ext=mp4]"
                print("⚠️ HD quality limited to 720p (FFmpeg not available)\n")
        
        
                
        # Folder making system block: if folder not exist then make folder for puting videos
        if not os.path.exists("DownloadYoutubeVideos"):
            os.makedirs("DownloadYoutubeVideos", exist_ok=True)
        
        
            
        # computer formating system block: computer set the formation and title and extension like .mp4
        self.ydl_object = yt_dlp.YoutubeDL({
            'format': format_str,
            'outtmpl': './DownloadYoutubeVideos/%(title)s.%(ext)s',
            'quiet': False,
            'no_warnings': True,
            "ffmpeg_location": None,
            
            
        })

            
            
        
        
        
        
    
    def Downloader(self):
        
        
    # computer calling block: the setup_downloader call and setup formation and user choose quality
        
        if not self.urls:
            print("No URLS To Download.")
            return
        
        # FFmpeg availability checking block: check once before setup
        ffmpeg_available = check_ffmpeg()
        
        self.setup_downloader(ffmpeg_available)
        
        
        # video donwload system block: urls check and taking info for using filename. and downloading batch of files giving by user
        for url in self.urls:
                
            
            # prepare name system block: prepare the file name and extra info
            try:
                
                info = self.ydl_object.extract_info(url, download=False)
                
                
            except yt_dlp.utils.DownloadError:
                print("Your Internet connection are weak")
                
            try:
                file_name = self.ydl_object.prepare_filename(info)
            
            except Exception as e:
                print(f"❌ Error checking URL: {str(e)}")
                continue
            
            
            
            # message print block: this message print for user to sure what video it is.
            print(f"Downloading: {file_name}")
            
            
            
            
            # download file system block: download the file own user computer
            self.ydl_object.download([url])







def quits(choice) -> bool:
    
    
    # exit decision system block: check if user wants to exit the program
    if choice.lower() in ["y", "yes"]:
        return False
    return True



    
# interface information block: takes list of urls until user by stopped ,  quality options hd or sd
def interface():
    
    links = []
    print("\n" + "="*60)
    print("Youtube Downloader Tool")
    print("="*60)
    
    
    
    
    # FFmpeg information block: show general information to user
    print("\nNote: FFmpeg is required for 1080p+ HD quality")
    print("      Without FFmpeg, HD limited to 720p")
    print("      SD videos work normally\n")
    print("-" * 60)
    
    while True:
    
    
        
        # url taking block: users gives lists of urls for download
        url = input("Paste the single Url or multiple Url (press enter to stop): ")
        
    
    
        
        # user by stopped system  block: if users have finish url links then press enter to continue process
        if url:
            links.append(url)
            print(f"\n✓ Added URL: {url}\n")
            continue
            
        
        else:
            break
            
            
        
          
        
        
    # quality option block: user can select the quality
    quality = input("Choose Quality (hd/sd): ").lower()
     
     
     
        
    # computer descision block: user choose options and computer watch and  assigned
    if quality == "sd":
        quality = "sd"  # default
        print("✓ SD quality selected")
        
    else:
        quality = "hd"
        print("✓ HD quality selected\n")
            
            
        
        
    # computer checking links block: user not giving urls then prints
    if not links:
        print("No URLs provided.")
        return
    
    
    
    
    # Download system block : download all list of files and single file
    downloader = YoutubeDownloader(links, quality)
    downloader.Downloader()
        
        
        
def check_ffmpeg() -> bool:
    # FFmpeg detection system block: check if ffmpeg is installed on user system
    
    try:
        
        
        # computer checking block: run ffmpeg command to check availability
        subprocess.run(['ffmpeg', '-version'],
                        capture_output=True,
                        text=True,
                        timeout=3)
        print("✓ FFmpeg detected: Full quality available (up to 4K)")
        return True
    
    
    
    except:
        # warning system block: if ffmpeg not found, show warning message
        print("\n⚠️ FFmpeg Not Found!")
        print("\nNote: Without FFmpeg, HD videos limited to 720p (single stream)")
        print("SD videos will work normally")
        return False
            
        
        
        
# Main program execution block: start the tool and run until user exits
while True:
    
    
    
    # Tool welcome system block: show welcome message once at start
    print("\n" + "="*60)
    print("Welcome to Youtube Downloader Tool")
    print("="*60)
    
    
    
    # FFmpeg initial check block: check once at start and show status
    ffmpeg_status = check_ffmpeg()
    
    
    
    
    # Run interface block: start the main user interface
    interface()
    
    
    
    # exit system block: user choice if continue the program
    choice = input("\nDo you want to download more videos? (y/n): ").lower()
    
    
    
    
    # computer descision block: check user choice
    if quits(choice):
        print("\n" + "="*60)
        print("Thanks for using my program!")
        print("="*60)
        break
    else:
        print("\n" + "-"*40)
        print("Starting new download session...")
        print("-"*40)