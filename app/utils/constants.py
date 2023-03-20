client_id_var = "STRAVA_CLIENT_ID"
client_secret_var = "STRAVA_CLIENT_SECRET"

base_url = "https://www.strava.com/api/v3/"

tacocat_image_url = "https://dgalywyr863hv.cloudfront.net/pictures/strava_o_auth/applications/56623/17689676/1/large.jpg"
sadbear_image_url = "http://1.bp.blogspot.com/_EWGdhFZYNDA/TIUpewCuKAI/AAAAAAAAAFU/WLgeFdSLWK0/s1600/contest_bear1.jpg"

home = 'home'
welcome = 'welcome'
invalid_permissions = 'invalid_permissions'
table = 'table'

# summary fields
athlete_summary_fields = {
    'firstname': 'name', 'premium': 'strava premium',
    'city': 'city', 'state':'state', 'created_at':'joined'
}
bikes_summary_fields = {
    'name':'name', 'primary':'primary', 'converted_distance': 'miles ridden'
}

# table fields
activities_fields = {'name': 'name', 'distance': 'distance (mi)', 'elapsed_time': 'total time', 'bike_name': 'bike',
    'total_elevation_gain': 'total elevation gain', 'sport_type': 'activity type', 'start_date_local': 'activity date',
    'trainer': 'trainer ride', 'average_speed': 'average speed (mph)',
    'max_speed': 'max speed (mph)', 'average_cadence': 'avg cadence', 'average_temp': 'avg temp (f)', 'average_watts': 'avg watts',
    'kilojoules':'kilojoules', 'average_heartrate':'avg hr', 'max_heartrate':'max hr', 'suffer_score':'relative effort'
}




# resource_state
# athlete
# name
# distance
# moving_time
# elapsed_time
# total_elevation_gain
# type
# sport_type
# workout_type
# id
# start_date
# start_date_local
# timezone
# utc_offset
# location_city
# location_state
# location_country
# achievement_count
# kudos_count
# comment_count
# athlete_count
# photo_count
# map
# trainer
# commute
# manual
# private
# visibility
# flagged
# gear_id
# start_latlng
# end_latlng
# average_speed
# max_speed
# average_cadence
# average_temp
# average_watts
# kilojoules
# device_watts
# has_heartrate
# average_heartrate
# max_heartrate
# heartrate_opt_out
# display_hide_heartrate_option
# elev_high
# elev_low
# upload_id
# upload_id_str
# external_id
# from_accepted_tag
# pr_count
# total_photo_count
# has_kudoed
# suffer_score
# max_watts
# weighted_average_watts