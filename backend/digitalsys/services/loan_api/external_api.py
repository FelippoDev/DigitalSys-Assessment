import requests

class LoanApiVerifier:
    _URL = "https://loan-processor.digitalsys.com.br/api/v1/"
    
    def loan_analysis(self, document, fullname):
        url = self._URL + 'loan/'
        body = {
            "document": document,
            "name": fullname,
        }
        
        response = requests.post(url, data=body).json()
        return response['approved']