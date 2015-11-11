'''
Spotify Controller

Copyright (c) 2015, Travis Kempbell

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
'''

import subprocess

class SpotifyController(object):

    @staticmethod
    def run_script(script):
        return subprocess.Popen([script], stdout=subprocess.PIPE, shell=True).communicate()[0].strip()

    # Application Getters
    def get_sound_volume(self):
        return int(self.run_script("osascript -e 'tell application \"Spotify\" to get sound volume'"))
    
    def get_player_state(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get player state'")
    
    def get_player_position(self):
        return float(self.run_script("osascript -e 'tell application \"Spotify\" to get player position'"))
    
    def get_repeating_enabled(self):
        return bool(self.run_script("osascript -e 'tell application \"Spotify\" to get repeating enabled'") in 'true')
    
    def get_repeating(self):
        return bool(self.run_script("osascript -e 'tell application \"Spotify\" to get repeating'") in 'true')
    
    def get_shuffling_enabled(self):
        return bool(self.run_script("osascript -e 'tell application \"Spotify\" to get shuffling enabled'") in 'true')
    
    def get_shuffling(self):
        return bool(self.run_script("osascript -e 'tell application \"Spotify\" to get shuffling'") in 'true')

    # Track Getters
    def get_artist(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get artist of current track'")
    
    def get_album(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get album of current track'")
    
    def get_disc_number(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get disc number of current track'")

    def get_duration(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get duration of current track'")

    def get_played_count(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get played count of current track'")
    
    def get_track_number(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get track number of current track'")
    
    def get_popularity(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get popularity of current track'")
    
    def get_id(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get id of current track'")
    
    def get_name(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get name of current track'")
    
    def get_artwork(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get artwork of current track'")
    
    def get_album_artist(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get album artist of current track'")
    
    def get_spotify_url(self):
        return self.run_script("osascript -e 'tell application \"Spotify\" to get spotify url of current track'")
                                
    # Setters
    def set_sound_volume(self, value):
        self.run_script("osascript -e 'tell application \"Spotify\" to set sound volume to %d'" % value)
    
    def set_player_position(self, value):
        # Value must be float
        self.run_script("osascript -e 'tell application \"Spotify\" to set player position to %.2f'" % float(value))
    
    def set_repeating(self, value):
        # Value must be boolean
        self.run_script("osascript -e 'tell application \"Spotify\" to set repeating to %d'" % int(value))
    
    def set_shuffling(self, value):
        # Value must be boolean
        self.run_script("osascript -e 'tell application \"Spotify\" to set shuffling to %d'" % int(value))
    
    def play_track(self, value):
        # Value must be Spotify URI
        self.run_script("osascript -e 'tell application \"Spotify\" to play track \"%s\"'" % value)
    
    def play(self):
        self.run_script("osascript -e 'tell application \"Spotify\" to play'")
    
    def pause(self):
        self.run_script("osascript -e 'tell application \"Spotify\" to pause'")
    
    def playpause(self):
        self.run_script("osascript -e 'tell application \"Spotify\" to playpause'")
    
    def next(self):
        self.run_script("osascript -e 'tell application \"Spotify\" to next track'")
    
    def previous(self):
        self.run_script("osascript -e 'tell application \"Spotify\" to previous track'")