#ScrapeCommand
    #init
    #execute

#FindNewCounselorsCommand
    #init
    #execute
    #create_new_counselor
    #append_url_format
    #exists_in_database

#CommandFactory
    #new_ScrapeCommand

#Adapter
    #init
    #convert_bad_encodings
    #update_all_now
    #update_now
    #schedule_update
    #updatedb
    #get_scheduled_updates
    #delete_scheduled_update
    #clear_all_scheduled_updates
