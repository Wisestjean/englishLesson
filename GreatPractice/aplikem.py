from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.metrics import dp




class DAshDrawer(MDBoxLayout):
    na_drawer = ObjectProperty()


class RoleSelectionScreen(Screen):
    def on_checkbox_active(self, role, value):
        if value:
            self.role = role
            
    def switch_to_selected_screen(self):
        if hasattr(self, 'role'):
            app.switch_screen(self.role + 's')


class LoginScreen(Screen):
    def switch_to_role_selection_screen(self):
        app.switch_screen('role_selection')
    # def __init__(self, **kw):
    #     super(LoginScreen, self).__init__(**kw)
    #     self.add_widget(MDRaisedButton(
    #         text="Login",
    #         pos_hint= {'center_x': 0.5,'center_y': 0.5},
    #         on_press=self.switch_to_teachers_screen
    #     ))
        
    def switch_to_teachers_screen(self, instance):
        app.switch_screen('teachers')


class RegisterScreen(Screen):
    def switch_to_role_selection_screen(self):
        app.switch_screen('role_selection')


class TeachersScreen(MDScreen):
    def switch_to_role_selection_screen(self):
        app.switch_screen('role_selection')
    # def __init__(self, **kw):
    #     super(TeachersScreen, self).__init__(**kw)
    #     self.add_widget(MDRaisedButton(
    #         text='Back to Login',
    #         pos_hint={'center_x': 0.5,'center_y': 0.5},
    #         on_press=self.switch_to_login_screen
    #     ))
        
    # def switch_to_login_screen(self, instance):
    #     app.switch_screen('login')
    def switch_to_screen(self, screen_name):
        app.root.ids.screen_manager.current = screen_name
        
        
    def create_edit_lesson(self):
        # Implement logic for creating/editing lessons
        app.root.ids.screen_manager.current = 'lesson_screen'

    def view_students_activity(self):
        # Implement logic for viewing students' activity
        app.root.ids.screen_manager.current = 'activity_screen'

    def messaging(self):
        # Implement messaging logic
        app.root.ids.screen_manager.current = 'messaging_screen'

    def check_students_progress(self):
        # Implement logic for checking students' progress
        app.root.ids.screen_manager.current = 'progress_screen'

    def show_notifications(self):
        # Implement logic for showing notifications
        print("Show Notifications")
    
    def switch_to_dashboard(self):
        app.root.ids.nav_drawer.set_state("close")
        app.root.ids.screen_manager.current = 'dashboard_screen'

    def logout(self):
        # Implement logout logic
        app.switch_screen('login')

# ***  CREATE THE SCRENS INSIDE OF TEACHER'DASHBOARD  ***

class LessonCreateScreen(Screen):
    def switch_to_screen(self):
        app.switch_screen('dashboard_screen')
        

class ActivityScreen(Screen):
    def switch_to_screen(self):
        app.switch_screen('dashboard_screen')
        

class MessagingScreen(Screen):
    def switch_to_screen(self):
        app.switch_screen('dashboard_screen')
        

class ProgressScreen(Screen):
    def switch_to_screen(self):
        app.switch_screen('dashboard_screen')
# ***  *********************************************  ***


class StudentsScreen(Screen):
    def switch_to_role_selection_screen(self):
        app.switch_screen('role_selection')


class LessonsScreen(Screen):
    def switch_to_role_selection_screen(self):
        app.switch_screen('role_selection')


class MyApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        # Builder.load_file('main.kv')
        Builder.load_file('main.kv')
        self.sm = ScreenManager()

        
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RoleSelectionScreen(name='role_selection'))       
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(TeachersScreen(name='teachers'))
        self.sm.add_widget(StudentsScreen(name='students'))
        self.sm.add_widget(LessonsScreen(name='lessons'))
        #ADD THE SCREEN INSIDE OF TEACHERS SCREEN
        self.sm.add_widget(LessonCreateScreen(name='lesson_screen'))
        

        return self.sm

    def switch_screen(self, screen_name):
        self.sm.current = screen_name


if __name__ == "__main__":
    app = MyApp()
    app.run()