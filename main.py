from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner

import cv2

def main():
    # Read Video
    video_frames = read_video(r"input_videos\08fd33_4.mp4")   


    #initialize tracker 
    tracker = Tracker("models/best.pt")

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path="stubs/track_stubs.pkl",)
    

    #interpolate ball positions
    tracks['ball'] = tracker.interpolate_ball_positions(tracks["ball"])


    # Assign player teams 
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0],
                                    tracks['players'][0])
    
    for frame_num, player_tracks in enumerate(tracks['players']):
        for player_id, track in player_tracks.items():
            team = team_assigner.get_player_team(video_frames[frame_num],
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_color[team]

            




    # Draw Output
    ## Draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save Video
    save_video(output_video_frames, "output_videos/output.avi")
    
if __name__ == '__main__':
    main()