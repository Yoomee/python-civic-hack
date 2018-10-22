from xml.dom import minidom
xmldoc = minidom.parse("FHRS706en-GB.xml")
list = xmldoc.getElementsByTagName("EstablishmentDetail")
for n in list:
  business = n.getElementsByTagName("BusinessName")[0].firstChild.data
  rating = n.getElementsByTagName("RatingValue")[0].firstChild.data

  if n.getElementsByTagName("RatingDate")[0].firstChild:
      date = n.getElementsByTagName("RatingDate")[0].firstChild.data

  print ("%s rated %s on %s" % (business, rating, date))
