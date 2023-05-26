
from Nkd.Foundation.Common.CallContext import CallContextManager
from flask import Flask
import traceback
import datetime



if __name__ == "__main__":
    app = Flask(__name__)


    with app.app_context():
        CallContextManager.Create()
        CallContextManager.GetCurrentCallContext().RequestUserName = 'System'
        CallContextManager.GetCurrentCallContext().CreateHistoryTransaction(0, 'System Deploy')
        
        try:    
            if None in 'dd':
                print("www")
            
            CallContextManager.GetCurrentCallContext().DbSession.commit()
            

        except Exception:
            CallContextManager.GetCurrentCallContext().DbSession.rollback()
            print(traceback.format_exc())
        finally:
            CallContextManager.GetCurrentCallContext().DbSession.close()