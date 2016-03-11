import json
import requests
import time
import unittest
import junitxml

def Ontobi_API(S1):
     DISPLAY_EVERY = 1
     url = 'http://52.72.120.188:8080/ontobi'
     payload = {"id":"hello","text":S1,"itemsToTag":"Integer|Name"}
     headers = {'content-type': 'application/json'}

     session = requests.Session()

     startall = time.time()
     for i in range(1):
      if i % DISPLAY_EVERY == (DISPLAY_EVERY - 1):
       start = time.time()
       r = session.post(url, data = json.dumps(payload), headers = headers)
       roundtrip = time.time() - start
       #sys.stdout.write("\n" + str(r.text) + "\n" + str(roundtrip))
       #sys.stdout.write("\n" + str(roundtrip))
     roundtripall = time.time() - startall
     #sys.stdout.write("\n" + str(roundtripall))
     j = json.loads(str(r.text))
     return str(j["data"]["bodyS2"])


class InequalityTest(unittest.TestCase):

    def test_Mail(self):
     text = "Hi Mr. John Davis The documentary by Ms. Julia H. Smith Of Miracles And Men, February 23, 2016 which was directed by Jonathan Hock, premiered on ESPN on February 8, 2016 as part of the channel's 30 for 30 series."
     expected="hi #n       davis the documentary by #n                 of miracles and men  february 23, 2016 which was directed by #n       hock  premiered on espn on february 8, 2016 as part of the channel's #  for #  series "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_equal3(self):
     text = "February 8, 2016 as part of the channel's 30 for 30 series."
     expected="february 8, 2016 as part of the channel's #  for #  series "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_Time(self):
     text = "2008-03-09 16:05:07 UniversalSortableDateTime"
     expected="2008-03-09 #t       universalsortabledatetime"
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_Name(self):
     text = "He thanks Professor Paulos for his insight. This ingenious scholar, teacher and author is a Professor at Temple University. As his long time colleague I assure you that he didn't generate esoteric knowledge and keep it for himself. "
     expected="he thanks professor #n     for his insight  this ingenious scholar  teacher and author is a professor at temple university  as his long time colleague i assure you that he didn't generate esoteric knowledge and keep it for himself  "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_Date(self):
     text    = "passed by the House on May 12, and the Senate on May 17 "
     expected= "passed by the house on #dt     and the senate on #dt    "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_CityStateWithPostal(self):
     text    = "New York weather forecast from AccuWeather.com. Extended forecast in New York, NY 10007 for up to 25 days includes high temperature"
     expected= "new york weather forecast from accuweather.com  extended forecast in #csp               for up to 25 days includes high temperature"
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_EmailWithBracket(self):
     text    = " From: Pergher, Gunther <Gunther.Pergher@dowjones.com> "
     expected= " from  pergher  gunther #emlb                          "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_Integer(self):
     text    = "much lower than the 200,000 anticipated on Wall Street"
     expected= "much lower than the #       anticipated on wall street"
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_DisclaimRemoval(self):
     text    = "The information contained in this communication is confidential and may contain information that is privileged or exempt from disclosure under applicable law. If you are not a named addressee, please notify the sender immediately and delete this email from your system.  If you have received this communication, and are not a named recipient, you are hereby notified that any dissemination, distribution or copying of this communication is strictly prohibited."
     expected= ""
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

    def test_Integer(self):
     text    = "193 Park Drive, 1st Floor"
     expected= "#addr1                   "
     Actuval=Ontobi_API(text)
     self.assertEqual(Actuval, expected)

if __name__ == '__main__':
    unittest.main()

