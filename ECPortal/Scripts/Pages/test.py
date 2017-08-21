'''
Created on Jul 26, 2017

@author: stetester
'''
from OSeries8.MyEnterpriseCertificatePortal import MyEnterpriseCertificatePortal
# MyEnterpriseCertificatePortal

if __name__ == '__main__':
    lib = {}
    p = MyEnterpriseCertificatePortal(lib)
    p.ECP_Approve_Or_Reject_Certificate(
        "Approved",
        "wCompany1@wcompany1.com",
        "HAWAII", "", ""

    )
    pass
