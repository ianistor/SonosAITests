from time import sleep
#!/usr/bin/env python
from soco import SoCo

if __name__ == '__main__':
    sonos = SoCo('192.168.1.229') # Pass in the IP of your Sonos speaker

    sonos.volume = 50

    sonos.play_uri('http://192.168.1.45:8000/sounds/caged_intro_2.mp3')
    sonos.play()

    sleep(12)

    sonos.play_uri('http://192.168.1.45:8000/sounds/caged_message_new_0.mp3')
    sonos.play()

    track = sonos.get_current_track_info()

    print (track['title'])

    # sonos.pause()


