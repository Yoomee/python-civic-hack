from xml.dom import minidom
xmldoc = minidom.parse("FHRS706en-GB.xml")
list = xmldoc.getElementsByTagName("EstablishmentDetail")

# Initialise counters
rating_1 = 0
rating_2 = 0
rating_3 = 0
rating_4 = 0
rating_5 = 0
no_rating = 0

for n in list:
  type = n.getElementsByTagName("BusinessType")[0].firstChild.data

  if type == "Restaurant/Cafe/Canteen":
      business = n.getElementsByTagName("BusinessName")[0].firstChild.data
      rating = n.getElementsByTagName("RatingValue")[0].firstChild.data
      if n.getElementsByTagName("RatingDate")[0].firstChild:
          date = n.getElementsByTagName("RatingDate")[0].firstChild.data

      # Increment counters
      if rating == "1":
        rating_1 += 1
      if rating == "2":
        rating_2 += 1
      if rating == "3":
        rating_3 += 1
      if rating == "4":
        rating_4 += 1
      if rating == "5":
        rating_5 += 1
      if rating == "AwaitingInspection":
        no_rating += 1

      print ("%s rated %s on %s" % (business, rating, date))

# Finished
print ("Total rated 1: %s" % (rating_1))
print ("Total rated 2: %s" % (rating_2))
print ("Total rated 3: %s" % (rating_3))
print ("Total rated 4: %s" % (rating_4))
print ("Total rated 5: %s" % (rating_5))
print ("Total not rated 1: %s" % (no_rating))
