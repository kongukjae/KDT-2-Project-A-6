import fromGovernmentAPIRefactoring
import fromInstagramRefactoring
import fromZooseyoRefactoring
import changeJsonData

def main():
    fromGovernmentAPIRefactoring.main()
    fromZooseyoRefactoring.main()
    fromInstagramRefactoring.main()
    changeJsonData.zooseyo()
    changeJsonData.insta()

main()