#account for accumulated times in running

def get_cur_hedons():
    '''return cur_hedons value'''
    global cur_hedons #hedons
    return cur_hedons

def get_cur_health():
    '''return cur_health value'''
    global cur_health #health points
    return cur_health

def offer_star(activity):
    '''offer a star for the passed activity
       activity: string
    '''
    global time_passed
    global star_count #helps determine if > 3 stars / min
    global times_stars_offered
    #list to determine if > 3 stars / min
    star_count += 1
    times_stars_offered.append(time_passed)
    #to ensure stars aren't given < 3times/ 120min
    star_can_be_taken(activity)

def perform_activity(activity, duration):
    '''perform given activity for duration
       activity = "resting", "running", or "textbooks"
       duration in minutes
    '''
    global cur_health #health points
    global cur_hedons #hedons
    global star_running #star for running = True or False
    global star_textbooks
    #star for textbooks = True or False
    global star_count #helps determine if > 3 stars / min
    global time_resting #adds up duration of resting
    global time_passed #adds up all the durations
    global tired #either True or False
    global time_running_3hp
    #if -ve then have been running for > 180min straight

    i = 1 #since we start at min 1, not min 0
    time_passed += duration

    #running block
    if activity == "running":
        while i <= duration: # <= since starts at 1
            if time_running_3hp > 0:
                cur_health += 3
            if time_running_3hp <= 0:
                cur_health += 1
            if tired == False: #hedons if not tired
                if i <= 10:
                    cur_hedons += 2
                if i > 10:
                    cur_hedons -=2
            if tired == True: #hedons if tired
                cur_hedons -= 2
            if star_running == True: #if have a star
                if i <= 10: #since only works for first 10min
                    cur_hedons += 3
            time_running_3hp -= 1
            i += 1
        time_resting = 0
        tired = True #since just finished an activity

    #textbook block
    if activity == "textbooks":
        while i <= duration:
            cur_health += 2
            if tired == False: #hedons if not tired
                if i <= 20:
                    cur_hedons += 1
                if i > 20:
                    cur_hedons -= 1
            if tired == True: #hedons if tired
                cur_hedons -= 2
            if star_textbooks == True: #if have a star
                if i <= 10: #since only works for first 10min
                    cur_hedons += 3
            i += 1
        time_resting = 0
        time_running_3hp = 180 #since not running straight
        tired = True #since just finished an activity

    #resting block
    if activity == "resting":
        time_resting += duration
        if time_resting >= 120:
            star_count = 0
            tired = False
        time_running_3hp = 180

    star_running = False
    #once this fuction runs, stars are no longer true
    star_textbooks = False

#to get untired must rest for 120min straight

def star_can_be_taken(activity):
    '''return True if the star can be taken
       star can be taken if < 3 stars offered in last 120min
    '''
    global star_running#star for running = True or False
    global star_textbooks
    #star for textbooks = True or False
    global star_count #helps determine if > 3 stars / min
    global times_stars_offered
    #list to determine if 3 stars / min
    if activity == "running":
        if len(times_stars_offered) <= 2:
        #since last entry is talking abt rn
            star_running = True
            #[1, 2]
        elif times_stars_offered[-3] > times_stars_offered[-1] - 120:
            star_running = False
            #[1, 2, 3]
        else:
            star_running = True
    if activity == "textbooks":
        if len(times_stars_offered) <= 2:
        #since last entry is talking abt rn
            star_textbooks = True
            #[1, 2]
        elif times_stars_offered[-3] > times_stars_offered[-1] - 120:
            star_textbooks = False
            #[1, 2, 3]
        else:
            star_textbooks = True
    if star_running == True or star_textbooks == True:
        return True
    else:
        return False

def most_fun_activity_minute():
    '''return the activity that will give the most hedons if duration = 1'''
    global tired #either True or False
    if tired == True:
        if star_running == True:
        #resting = 0, running w star = 1
            return "running"
        if star_textbooks == True:
        #resting = 0, textbook w star = 1
            return "textbooks"
        return "resting"
        #resting = 0, running and textbook = -2
    if tired == False:
        if star_running == True:
        #resting = 0, running w star = 5
            return "running"
        if star_textbooks == True:
        #resting = 0, textbook w star = 4
            return "textbooks"
        return "running"

def initialize ():
    '''define all global variables and give initial values'''
    global cur_health #health points
    global cur_hedons #hedons
    global star_running #star for running = True or False
    global star_textbooks
    #star for textbooks = True or False
    global star_count #helps determine if > 3 stars / min
    global time_resting #adds up duration of resting
    global time_passed #adds up all the durations
    global times_stars_offered
    #list to determine if > 3 stars / min
    global tired #either True or False
    global time_running_3hp
    #if -ve then have been running for > 180min straight/
    #if 0 or -ve hp += 1 instead of += 3
    cur_health = 0
    cur_hedons = 0
    star_running = False
    star_textbooks = False
    star_count = 0
    time_resting = 0
    time_passed = 0
    times_stars_offered = []
    tired = False
    time_running_3hp = 180

initialize()

if __name__ == "__main__":
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3
    print(most_fun_activity_minute()) #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute()) #running
    perform_activity("textbooks", 30)
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    #COMMENT BY ME 1 hedon first 10, -2 hedons 2nd 10
    print(get_cur_health()) # 210 = 150 + 20 * 3
    print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons()) # -430 = -90 + 170 * (-2)
    offer_star("running")

#my test code with star texbook
    # initialize()
    # perform_activity("running", 30)
    # print(get_cur_hedons()) # -20 = 10 * 2 + 20 * (-2)
    # print(get_cur_health()) # 90 = 30 * 3
    # print(most_fun_activity_minute()) #resting
    # perform_activity("resting", 30)
    # offer_star("textbooks")
    # print(most_fun_activity_minute()) #textbooks
    # perform_activity("textbooks", 30)
    # print(get_cur_health()) # 150 = 90 + 30*2
    # print(get_cur_hedons()) # -50 = -20 + 30 * (-2)
    # offer_star("running")
    # perform_activity("running", 20)
    # #COMMENT BY ME 1 hedon first 10, -2 hedons 2nd 10
    # print(get_cur_health()) # 210 = 150 + 20 * 3
    # print(get_cur_hedons()) # -90 = -80 + 10 * (3-2) + 10 * (-2)
    # perform_activity("running", 170) #Star works because when change this to 17 star_running = False
    # print(get_cur_health()) # 700 = 210 + 160 * 3 + 10 * 1
    # print(get_cur_hedons()) # -430 = -90 + 170 * (-2)
    # offer_star("running")

    # initialize()
    # perform_activity("running", 30)
    # get_cur_hedons() # -20 = 10 * 2 + 20 * (-2)
    # get_cur_health() # 90 = 30 * 3
    # most_fun_activity_minute() #resting
    # perform_activity("resting", 30)
    # offer_star("running")
    # most_fun_activity_minute() #running
    # perform_activity("textbooks", 30)
    # get_cur_health() # 150 = 90 + 30*2
    # get_cur_hedons() # -80 = -20 + 30 * (-2)
    # offer_star("running")
    # perform_activity("running", 20)
    # #COMMENT BY ME 1 hedon first 10, -2 hedons 2nd 10
    # get_cur_health() # 210 = 150 + 20 * 3
    # get_cur_hedons() # SHOULD BE -90
    # perform_activity("running", 170)
    # get_cur_health() # 700 = 210 + 160 * 3 + 10 * 1
    # get_cur_hedons() # -430 = -90 + 170 * (-2)
    # offer_star("running")

 # # Test Star behaviour
 #    initialize()
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # running
 #
 #    initialize()
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks
 #    offer_star("textbooks")
 #    perform_activity("running", 30)
 #    print(most_fun_activity_minute()) # resting
 #
 #    initialize()
 #    offer_star("textbooks")
 #    perform_activity("running", 101)
 #    print(get_cur_health()) # 303
 #    print(get_cur_hedons()) # -162
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks
 #    perform_activity("textbooks", 20)
 #    offer_star("textbooks")
 #    print(most_fun_activity_minute()) # textbooks


