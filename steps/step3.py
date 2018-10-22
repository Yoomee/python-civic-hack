from xml.dom import minidom
xmldoc = minidom.parse("FHRS706en-GB.xml")
list = xmldoc.getElementsByTagName("EstablishmentDetail")
for n in list:
  business = n.getElementsByTagName("BusinessName")[0].firstChild.data
  rating = n.getElementsByTagName("RatingValue")[0].firstChild.data

  if rating == "0":
    print ("%s %s" % (business, rating))
