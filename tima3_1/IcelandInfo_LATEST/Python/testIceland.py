import sys
from IcelandInfo_LATEST.Python.iceconnect import *


def valmynd():
    running = True
    places = PlaceDB()
    hotel = HotelDB()
    restaurant = RestaurantDB()
    activity = ActivitylDB()
    utility = Utility()
    while (running):
        inside = True
        print()
        print("Hotel [1]")
        print("Places [2]")
        print("Restaurants [3]")
        print("Activities [4]")
        print("Utilities(Social media) [5]")
        val = int(input("Type here: "))
        if (val == 1):
            while(inside):
                inside2 = True
                print()
                print("Create [1]")
                print("Read [2]")
                print("Update [3]")
                print("Delete [4]")
                print("Print all [5]")
                print("Back [6]")
                crud = int(input("Type here: "))
                if(crud == 1):
                    #Hótel gummi,Ægisgrund 12,Gummi Jónsson,https://www.mbl.is,gummi@gummihotels.is, 354-4602000, 112
                    print("Add hotel(put it all in ONE! line, no \"): [NAME], [ADDRESS], [MANAGER], [WEB], [EMAIL], [PHONE], [DIST]")
                    h = input("Type here: ")
                    hlist = [x.strip() for x in h.split(',')]
                    hotel.add_hotel(hlist[0],hlist[1],hlist[2],hlist[3],hlist[4],hlist[5],int(hlist[6]))

                elif(crud == 2):
                    id = int(input("Type hotel id here: "))
                    print(hotel.get_hotel(id))

                elif (crud == 3):
                    while(inside2):
                        print()
                        print("Add social media  [1]")
                        print("Remove hotel media [2]")
                        print("Update hotel [3]")
                        print("Update hotel coordinates [4]")
                        print("Back [5]")
                        update = int(input("Type here: "))
                        if(update == 1):
                            #6, 1, https://www.facebook.com/Gummishotels/
                            print("Add hotel media(put it all in ONE! line, no \"): [HOTEL_ID], [MEDIA_ID], [MEDIA_URL]")
                            h = input("Type here: ")
                            hlist = [x.strip() for x in h.split(',')]
                            print(hlist[0],hlist[1],hlist[2])
                            hotel.add_hotel_media(int(hlist[0]),int(hlist[1]),hlist[2])
                        elif (update == 2):

                            pass
                        elif (update == 3):
                            pass
                        elif (update == 4):
                            pass
                        elif (update == 5):
                            inside2 = False
                        else:
                            print("Not a valid option!")

                elif (crud == 4):
                    id = int(input("Type hotel id here: "))
                    h = hotel.get_hotel(id)
                    hotel.delete_hotel(id)
                    print("Deleted hotel: ", h)
                elif (crud == 5):
                    print(hotel.get_hotel_list())
                elif (crud == 6):
                    inside = False
                else:
                    print("Not a valid option!")



        if (val == 2):
            while (inside):
                print()
                print("Create [1]")
                print("Read [2]")
                print("Update [3]")
                print("Delete [4]")
                print("Print all [5]")
                print("Back [6]")
                crud = int(input("Type here: "))
                if (crud == 1):
                    #Garðabaer, höfuðborgarsvaedid, 15000, https://gardabaer.is/
                    print("Add place(put it all in ONE! line, no \"): [NAME], [REGION], [POPULATION], [WEB]")
                    p = input("Type here: ")
                    plist = [y.strip() for y in p.split(',')]
                    places.add_place(plist[0], plist[1], plist[2], plist[3])
                elif (crud == 2):
                    id = int(input("Type id place here: "))
                    print(places.get_place(id))
                elif (crud == 3):
                    pass

                elif (crud == 4):
                    id = int(input("Type Place ID you want to delete here: "))
                    p = places.get_place(id)
                    places.delete_place(id)
                elif (crud == 5):
                    print(places.get_place_list())
                elif (crud == 6):
                    inside = False
                else:
                    print("Not a valid option!")

        if (val == 3):
            while (inside):
                print()
                print("Create [1]")
                print("Read [2]")
                print("Update [3]")
                print("Delete [4]")
                print("Print all [5]")
                print("Back [6]")
                crud = int(input("Type here: "))
                if (crud == 1):
                    pass
                elif (crud == 2):
                    pass

                elif (crud == 3):
                    pass

                elif (crud == 4):
                    pass
                elif (crud == 5):
                    print(restaurant.get_restaurant_list())
                elif (crud == 6):
                    inside = False
                else:
                    print("Not a valid option!")

        if (val == 4):
            while (inside):
                print()
                print("Create [1]")
                print("Read [2]")
                print("Update [3]")
                print("Delete [4]")
                print("Print all [5]")
                print("Back [6]")
                crud = int(input("Type here: "))
                if (crud == 1):
                    pass
                elif (crud == 2):
                    pass

                elif (crud == 3):
                    pass

                elif (crud == 4):
                    pass
                elif (crud == 5):
                    pass
                elif (crud == 6):
                    inside = False
                else:
                    print("Not a valid option!")

        if (val == 5):
            while (inside):
                print()
                print("Create [1]")
                print("Read [2]")
                print("Update [3]")
                print("Delete [4]")
                print("Print all [5]")
                print("Back [6]")
                crud = int(input("Type here: "))
                if (crud == 1):
                    pass
                elif (crud == 2):
                    pass

                elif (crud == 3):
                    pass

                elif (crud == 4):
                    pass
                elif (crud == 5):
                    pass
                elif (crud == 6):
                    inside = False
                else:
                    print("Not a valid option!")

valmynd()