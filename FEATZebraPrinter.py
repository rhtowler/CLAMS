"""
FEAT specific instructions for printing labels

created by: Alicia Billings; alicia.billings@noaa.gov
date: April 2019
notes:
"""

from simple_zpl2 import Code128_Barcode, ZPLDocument, NetworkPrinter
import io
from PIL import Image
from datetime import datetime as dt
import socket


class PrintLabel:
    def __init__(self, ship, survey, ip='192.168.0.124', port=9100):
        self.ship = ship
        self.survey = survey
        self.ip = '192.168.0.124'
        self.port = int(port)

    def printer_status(self):
        """
        tests that the printer can be connected to
        :return: boolean True for yes, False for no
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            s.close()
            return True
        except Exception as e:
            print(e)
            return False

    def print_label(self, project, species_name, species_code, event, code, spec_num=None, length=None, weight=None):
        """
        takes the passed information and sends to the printer
        :param project: name of the project
        :param species_name: name of the species
        :param species_code: code of the species
        :param event: event number
        :param code: barcode zpl
        :return: none
        """
        # get current date
        cur_date = dt.now().date().strftime("%m/%d/%Y")

        # set up barcode
        bc = Code128_Barcode(code, 'N', 100, 'Y')

        z_doc = ZPLDocument()
        z_doc.add_zpl_raw("^XA")
        z_doc.add_zpl_raw("^FO5,55")
        z_doc.add_zpl_raw("^A0N,110,40^FDNWFSC/FEAT Sample\tHaul: " + str(event))
        if spec_num:
            z_doc.add_zpl_raw("\tSpecNum: " + str(spec_num) + "^FS")
        else:
            z_doc.add_zpl_raw("^FS")
        z_doc.add_zpl_raw("^FO5,170")
        z_doc.add_zpl_raw("^A0N,80,35^FDProject: " + str(project) + "\tSpecies: " + species_code + " - " + species_name + "^FS")
        if length:
            z_doc.add_zpl_raw("^FO5,240")
            z_doc.add_zpl_raw("^A0N,80,35^FSLength: " + str(length))
            if weight:
                z_doc.add_zpl_raw("\tWeight: " + str(weight) + "^FS")
            else:
                z_doc.add_zpl_raw("^FS")
        z_doc.add_zpl_raw("^FO5,325")
        z_doc.add_zpl_raw("^A0N,80,50^BCN,80,Y,N,N")
        z_doc.add_zpl_raw("^FD" + str(code) + "^FS")
        # z_doc.add_barcode(bc)
        z_doc.add_zpl_raw("^FO5,500")
        z_doc.add_zpl_raw("^A0N,50,25^FDSurvey: " + self.survey + "\t\tShip: " + self.ship + "\tDate: " + str(cur_date) + "^FS")
        z_doc.add_zpl_raw("^XZ")
        """
        bc = Code128_Barcode(code, 'N', 100, 'Y')

        z_doc = ZPLDocument()
        z_doc.add_zpl_raw("^FO0,60")
        z_doc.add_zpl_raw("^A2N50,30^FDNWFSC/FEAT Sample^FS")
        z_doc.add_zpl_raw("^FO0,130")
        z_doc.add_zpl_raw("^A2N50,30^FDHaul: " + str(event) + "\tDate: " + str(cur_date) + "^FS")
        z_doc.add_zpl_raw("^FO0,190")
        z_doc.add_zpl_raw("^A2N50,30^FDSurvey: " + self.survey + "\tShip: " + self.ship + "^FS")
        z_doc.add_zpl_raw("^FO0,260")
        z_doc.add_zpl_raw("^^A2N50,30^FDProject: " + project + "^FS")
        z_doc.add_zpl_raw("^FO0,330")
        z_doc.add_zpl_raw("^A2N50,30^FDSpecies: " + species_code + " - " + species_name + "^FS")
        z_doc.add_zpl_raw("^FO200,400")
        z_doc.add_barcode(bc)
		"""
		
        # print it out to the screen as an image for now
        #png = z_doc.render_png(label_width=2, label_height=1)
        #fake_file = io.BytesIO(png)
        #img = Image.open(fake_file)
        #img.show()

        # print to network printer
        printer = NetworkPrinter(self.ip, self.port)
        printer.print_zpl(z_doc)
