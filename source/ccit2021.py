import argparse  # 參數解析使用
import os
from Option import Option
from functions.Clock import Clock
from functions.encryption import cryto
from functions.shut import shut
from functions.Ipconfig import Showip
from functions.Nslookup import Nslookup
from functions.PortScanner import Scanport
import webbrowser 


def main():
    # 準備參數解析
    app_description = "校園資安測試常用工具集合"
    epilog_text = "歡迎至https://github.com/TwMoonBear-Arsenal/BetterCalculator/issues提供建議"
    parser = argparse.ArgumentParser(
        description=app_description, epilog=epilog_text)
    args = parser.parse_args()

    # 準備選單
    optionList = []
    optionList.append(Option(1, "顯示今天日期"))
    optionList.append(Option(2, "顯示本地端IP地址"))
    optionList.append(Option(3, "維吉尼亞_解密"))
    optionList.append(Option(4, "維吉尼亞_加密"))
    optionList.append(Option(5, "RSA_加密"))
    optionList.append(Option(6, "RSA_解密"))
    optionList.append(Option(7, "RSA_建立金鑰"))
    optionList.append(Option(8, "LSFR_加密&解密"))
    optionList.append(Option(9, "木棒_加密"))
    optionList.append(Option(10, "木棒_解密"))
    optionList.append(Option(3, "ip或hostname相互反查"))
    optionList.append(Option(4, "詢找目標主機有開啟的port"))
    optionList.append(Option(77,"surprise"))
    optionList.append(Option(87, "Do you want know who is Simon?"))
    print()

    while(True):

        # 顯示選單
        os.system('cls')
        print(app_description)
        print(epilog_text)
        print("--------")
        for option in optionList:
            print("[", option.number, "] ", option.descritpion)
        print("[", 99, "]", " 結束程式")

        # 詢問使用者
        selection = input("請輸入需要的功能：").strip()
        if(selection == "1"):
            Clock.ShowTime()
        elif(selection == "2"):
            Showip.ipconfig()
        elif(selection == "3"):
            cryto.decryp_Vige()
        elif(selection == "4"):
            cryto.encryp_Vige()
        elif(selection == "5"):
            cryto.rsa_send()
        elif(selection == "6"):
            cryto.rsa_read()
        elif(selection == "7"):
            cryto.Make_a_rsa()
        elif(selection == "8"):
            cryto.linr_radom()
        elif(selection == "9"):
            cryto.wood_encry()
        elif(selection == "10"):
            cryto.wood_decry()
        elif(selection == "77"):
            shut.shut()
        elif(selection == "87"):
            webbrowser.open("https://www.facebook.com/simon.lin.56829")
            for i in range(1,100):
               print('878787878787 "Simon" db2')
            nslookup_selection = input("\033[33mchoose type you want to use:\033[0m\n[1]hostname2ip\n[2]ip2hostname\n").strip()
            #print(nslookup_selection)
            if(nslookup_selection == "1"):
                Nslookup.domainip()
            else:
                Nslookup.ipdomain()
        elif(selection == "4"):
            portscanner_selection = input("\033[33mchoose type you want to use:\033[0m\n[1]TCP\n[2]UDP\n").strip()
            if(portscanner_selection == "1"):
                Scanport.portscannerTCP()
            else:
                Scanport.portscannerUDP()
        elif(selection == "99"):
            print("See you next time...")
            print()
            return
        else:
            print("輸入錯誤")

        # 開始下一循環
        input("按任意鍵繼續...")


if __name__ == "__main__":
    main()
