# Youtube-Video-Downloader
Youtube Video Downloader - A powerful tool to download YouTube videos in multiple qualities (HD/SD). Supports batch downloads, FFmpeg optimization, automatic quality detection, and organized file management.


# Youtube Video Downloader 🎬

A powerful, user-friendly tool to download YouTube videos in multiple quality options. Features batch downloading, automatic quality optimization, FFmpeg integration, and intelligent error handling.

## Features ✨

- 🎥 **Multiple Quality Options** - HD (1080p) and SD (480p) downloads
- ⚡ **Batch Download** - Download multiple videos at once
- 🔍 **FFmpeg Integration** - Automatic detection for optimal quality
- 📁 **Auto-Folder Creation** - Organized video storage
- 🏷️ **Original Titles** - Files saved with video titles
- ⚠️ **Error Handling** - Network issues handled gracefully
- 💾 **MP4 Format** - Standard compatible format
- 🎯 **Quality Detection** - Smart format selection based on availability
- 🔄 **Continuous Mode** - Download multiple batches without restarting

## Quality Options 📊

### HD Quality (1080p)
- **With FFmpeg**: Up to 1080p with separate video+audio streams
- **Without FFmpeg**: Limited to 720p (single stream)
- Best for: Movies, tutorials, high-quality content

### SD Quality (480p)
- Lower file size
- Faster downloads
- Works without FFmpeg
- Best for: Quick downloads, mobile viewing

## Installation 🚀

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Required Dependencies

```bash
pip install yt-dlp
```

### Optional (For Full HD Quality)

FFmpeg is optional but recommended for 1080p+ downloads:

**Windows:**
```bash
# Using chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

**Linux (Fedora):**
```bash
sudo dnf install ffmpeg
```

### Setup

```bash
# Clone the repository
git clone https://github.com/good123453/Youtube-Video-Downloader.git
cd Youtube-Video-Downloader

# Install dependencies
pip install yt-dlp

# Run the tool
python3 Youtube_Video_Downloader.py
```

## Usage 🎯

### Running the Tool

```bash
python3 Youtube_Video_Downloader.py
```

### Step-by-Step Guide

1. **Start the Tool**
   ```
   Welcome to Youtube Downloader Tool
   ```

2. **FFmpeg Check**
   - Tool automatically detects FFmpeg
   - Shows available quality options

3. **Add URLs**
   ```
   Paste the single Url or multiple Url (press enter to stop):
   ```
   - Paste one YouTube URL at a time
   - Press Enter after each URL
   - Leave blank and press Enter when done

4. **Select Quality**
   ```
   Choose Quality (hd/sd):
   ```
   - Type `hd` for HD quality (1080p or 720p)
   - Type `sd` for SD quality (480p)

5. **Download**
   - Videos download to `DownloadYoutubeVideos` folder
   - Filenames are original video titles
   - Progress shown in real-time

6. **Continue or Exit**
   ```
   Do you want to download more videos? (y/n):
   ```
   - Type `y` or `yes` for another session
   - Type `n` or `no` to exit

## Example Workflow 📋

```
============================================================
Welcome to Youtube Downloader Tool
============================================================

✓ FFmpeg detected: Full quality available (up to 4K)

============================================================
Youtube Downloader Tool
============================================================

Note: FFmpeg is required for 1080p+ HD quality
      Without FFmpeg, HD limited to 720p
      SD videos work normally

------------------------------------------------------------
Paste the single Url or multiple Url (press enter to stop): 
https://www.youtube.com/watch?v=dQw4w9WgXcQ

✓ Added URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Paste the single Url or multiple Url (press enter to stop): 
https://www.youtube.com/watch?v=9bZkp7q19f0

✓ Added URL: https://www.youtube.com/watch?v=9bZkp7q19f0

Paste the single Url or multiple Url (press enter to stop): 
(press Enter to stop)

Choose Quality (hd/sd): hd
✓ HD quality selected

✓ FFmpeg detected: Full quality available (up to 4K)
✓ HD quality selected (up to 1080p with FFmpeg)
Downloading: Never Gonna Give You Up.mp4
Downloading: Video Title 2.mp4

Do you want to download more videos? (y/n): n

============================================================
Thanks for using my program!
============================================================
```

## Code Structure 🏗️

### Main Components

#### `YoutubeDownloader` Class
- **`__init__`** - Initialize with URLs and quality
- **`setup_downloader`** - Configure quality settings
- **`Downloader`** - Execute the download process

#### `check_ffmpeg()` Function
- Detects FFmpeg installation
- Determines available quality options
- Returns boolean status

#### `interface()` Function
- Handles user input
- Manages URL collection
- Quality selection
- Initiates download process

#### `quits()` Function
- Processes exit decision
- Enables continuous mode

## Quality Selection Logic 🎨

```
Quality Selection Flow:

User Input (HD/SD)
      ↓
FFmpeg Check
      ↓
  ├─ If SD: 480p format
  └─ If HD:
     ├─ FFmpeg Found: 1080p (video+audio)
     └─ FFmpeg Not Found: 720p (single stream)
      ↓
Download Execution
```

## File Organization 📂

```
Youtube-Video-Downloader/
├── Youtube_Video_Downloader.py
├── README.md
├── .gitignore
├── LICENSE
└── DownloadYoutubeVideos/  (auto-created)
    ├── Video Title 1.mp4
    ├── Video Title 2.mp4
    └── ...
```

## Features Explained 💡

### Batch Downloading
- Add multiple URLs before starting
- All videos download in sequence
- Original titles preserved

### Quality Optimization
- **FFmpeg Available**: Video and audio merged separately for best quality
- **FFmpeg Not Available**: Single high-quality stream (limited to 720p)
- **SD Mode**: Fast download with lower file size

### Error Handling
- Network connection issues caught
- Invalid URLs handled gracefully
- Missing FFmpeg detected automatically

### Auto-Organization
- Creates `DownloadYoutubeVideos` folder automatically
- Files saved with original video titles
- MP4 format for maximum compatibility

## Troubleshooting 🔧

### "ModuleNotFoundError: No module named 'yt_dlp'"
```bash
pip install yt-dlp
```

### "FFmpeg Not Found" Warning
This is normal! You can still download:
- ✅ SD videos (full quality)
- ⚠️ HD videos (limited to 720p)

To fix, install FFmpeg:
- Windows: Download from https://ffmpeg.org
- Mac: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

### Download Speed Slow
- Check internet connection
- Try SD quality instead
- YouTube might be throttling (wait and retry)

### "Invalid URL" Error
- Verify YouTube URL is correct
- Check internet connection
- URL might be age-restricted or private

### Permission Denied Error
```bash
# On Windows: Run as Administrator
# On Linux/Mac:
chmod +x Youtube_Video_Downloader.py
```

### Videos Won't Download
- Check if video is available in your region
- Verify internet connection
- Try updating yt-dlp:
  ```bash
  pip install --upgrade yt-dlp
  ```

## Performance 🚀

- **Download Speed**: Depends on internet and video size
- **Batch Processing**: Sequential download (one at a time)
- **File Size**: 
  - SD: ~100-300MB per hour
  - HD: ~500MB-1.5GB per hour
- **Quality**: Best available for selected option

## Supported Formats 📹

- **Video Format**: MP4 (H.264 codec)
- **Audio Format**: AAC (included in MP4)
- **Resolution**: 480p (SD) to 1080p (HD)
- **Frame Rate**: Up to 60fps

## Limitations ⚠️

- YouTube ToS: Personal use only
- Age-restricted videos: May require account
- Regional restrictions: Depend on location
- Private videos: Cannot download
- Streaming-only content: May not work
- Download speed: Limited by YouTube/ISP

## Best Practices 👍

1. **Check File Size** - Ensure sufficient disk space
2. **Use HD for Quality** - Better for archival
3. **Use SD for Speed** - Faster downloads
4. **Batch Download** - Multiple URLs at once
5. **Organize Files** - Videos stored in dedicated folder
6. **Keep Updated** - Update yt-dlp regularly

## Future Enhancements 🔮

- 🎵 Audio-only download option
- 📊 Download progress bar
- 🎯 Quality preview before download
- 📋 Download queue management
- 🌐 Playlist support
- 🔐 Password-protected video handling
- 📝 Download history log
- ⚙️ Custom output folder

## Author 👨‍💻

Created by **good123453/Neo**

**Roles:**
- Project Lead & Developer
- Code Architect
- Main Programmer
- Tester & Debugger
- Documentation Writer

**AI Advisor:** Deepseek v3.2 Model
- Technical Advisor
- Code Reviewer
- Error Analyst
- Solution Consultant

## Credits 🙏

- **yt-dlp** - https://github.com/yt-dlp/yt-dlp
- **FFmpeg** - https://ffmpeg.org
- **Python Community** - For amazing libraries
- **YouTube** - For the platform

## License 📄

MIT License - See LICENSE file for details

Free to use for personal purposes.

## Support 💬

Issues or questions?
- 📖 Check the troubleshooting section
- 🐛 Open a GitHub issue
- 💡 Suggest improvements
- ⭐ Star the repository

## Important Notes ⚖️

### Legal Disclaimer
- ✅ Download for personal use only
- ✅ Respect creators' rights
- ✅ Follow YouTube's Terms of Service
- ❌ Do NOT use for commercial purposes without permission
- ❌ Do NOT redistribute downloaded content
- ❌ Do NOT bypass regional restrictions

### Ethical Usage
This tool should be used responsibly to download:
- ✅ Your own content
- ✅ Educational material
- ✅ Public domain content
- ✅ Content you have permission to download

---

**Happy Downloading! 🎉**

**Enjoy your favorite videos offline!** 📺

**Made with ❤️ for video enthusiasts!**
