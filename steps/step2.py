from xml.dom import minidom
xmldoc = minidom.parse("FHRS706en-GB.xml")
list = xmldoc.getElementsByTagName("EstablishmentDetail")
for n in list:
 business = n.getElementsByTagName("BusinessName")[0].firstChild.data
 print (business)
