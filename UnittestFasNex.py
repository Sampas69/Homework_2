import unittest
#import sys

from FastaNexus import read_fasta, nexus_header, nexus_body
test = "C:/Users/saras/Documents/ASB/Seq1test.fasta"

class TestFastaToNexus(unittest.TestCase):

    def test_read_fasta(self):
        result = read_fasta(test)
        self.assertEqual({'Seq1': 'ATGAAGGTTCCCC', 'Seq2':'ATGCCCTTGGAAG'}, result)

    def test_nexus_header(self):
        expected = "#Nexus\n\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=13;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX"
        result = nexus_header({'Seq1': 'ATGAAGGTTCCCC', 'Seq2':'ATGCCCTTGGAAG'})
        self.assertEqual(result, expected)


    def test_nexus_matrix(self):
        expected = "Seq1    ATGAAGGTTCCCC\nSeq2    ATGCCCTTGGAAG\n\nEND;"
        result = nexus_body({'Seq1': 'ATGAAGGTTCCCC', 'Seq2':'ATGCCCTTGGAAG'})
        self.assertEqual(result,expected)

if __name__ == '__main__':
    #my_test = TestFastaToNexus(test)
    #my_test.test_read_fasta()
    #my_test.test_nexus_header()
    #my_test.test_nexus_matrix()
    unittest.main()
#https://www.dio.me/articles/teste-unitario-em-python-com-unittest
