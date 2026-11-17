from tools import container
from tools.helper import shell
from tools.logger import Logger


class AndroidId:
   def get_id(self):
        if container.is_running():
            try:
                queryout = shell(
                    arg="sqlite3 /data/data/com.google.android.gsf/databases/gservices.db \"select * from main where name = 'android_id';\"",
                    env="ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n"
                )
            except:
                return
        else:
            Logger.error("Please make sure Waydroid is running and Gapps has been installed!")
            return
        android_id = queryout.replace("android_id|", "").strip()
        if not android_id:
            Logger.error("Android ID not found. Make sure GApps is installed and Play Store has been opened once.")
            return
        print(android_id)
        print("   ^----- Open https://google.com/android/uncertified/?pli=1")
        print("          Login with your google id then submit the form with id shown above")
