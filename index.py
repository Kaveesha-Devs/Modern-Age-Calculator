import ttkbootstrap as ttk # type: ignore from ttkbootstrap.constants import * # type:ignore 
import tkinter as tk
from tkinter import BOTH, X, LEFT, RIGHT, HORIZONTAL
from datetime import datetime
from tkinter import messagebox
import threading
import time

class ModernAgeCalculator:
    def __init__(self):
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.setup_animations()
        
    def setup_window(self):
        """Create ultra-modern window with custom styling"""
        self.app = ttk.Window(themename="cyborg")
        self.app.title("✨ Ultra Modern Age Calculator")
        self.app.geometry("600x750")
        self.app.resizable(False, False)
        
        # Custom window styling
        style = ttk.Style()
        style.configure('Modern.TLabel', font=('Segoe UI', 12))
        style.configure('Title.TLabel', font=('Segoe UI', 28, 'bold'))
        style.configure('Subtitle.TLabel', font=('Segoe UI', 11))
        style.configure('Card.TLabel', font=('Segoe UI', 10, 'bold'))
        style.configure('Result.TLabel', font=('Segoe UI', 14, 'bold'))
        style.configure('BigResult.TLabel', font=('Segoe UI', 20, 'bold'))
        
    def create_variables(self):
        """Initialize all StringVar variables"""
        self.age_result = tk.StringVar()
        self.years_result = tk.StringVar()
        self.months_result = tk.StringVar()
        self.days_result = tk.StringVar()
        self.hours_result = tk.StringVar()
        self.minutes_result = tk.StringVar()
        self.total_days_result = tk.StringVar()
        self.total_weeks_result = tk.StringVar()
        self.birthday_result = tk.StringVar()
        self.progress_text = tk.StringVar()
        self.zodiac_result = tk.StringVar()  # Fixed: Added missing zodiac_result variable
        
    def create_widgets(self):
        """Create all UI widgets with modern styling"""
        # Main container with gradient-like effect
        self.main_container = ttk.Frame(self.app)
        self.main_container.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        self.create_header()
        self.create_input_section()
        self.create_results_grid()
        self.create_additional_info()
        self.create_footer()
        
    def create_header(self):
        """Create modern header with gradient-style title"""
        header_frame = ttk.Frame(self.main_container)
        header_frame.pack(fill=X, pady=(0, 30))
        
        # Main title with modern styling
        title_frame = ttk.Frame(header_frame)
        title_frame.pack()
        
        title = ttk.Label(
            title_frame,
            text="⚡ AGE CALCULATOR",
            style='Title.TLabel',
            bootstyle="light"
        )
        title.pack()
        
        # Animated subtitle
        subtitle = ttk.Label(
            title_frame,
            text="✨ Discover your journey through time with precision ✨",
            style='Subtitle.TLabel',
            bootstyle="info"
        )
        subtitle.pack(pady=(5, 0))
        
        # Modern separator line
        separator = ttk.Separator(header_frame, orient=HORIZONTAL)
        separator.pack(fill=X, pady=(15, 0))
        
    def create_input_section(self):
        """Create modern input section with floating labels effect"""
        input_container = ttk.LabelFrame(
            self.main_container,
            text="🎯 Enter Your Birth Date",
            padding=25,
            bootstyle="primary"
        )
        input_container.pack(fill=X, pady=(0, 25))
        
        # Input instruction
        instruction = ttk.Label(
            input_container,
            text="Select your date of birth to unlock your time statistics",
            font=('Segoe UI', 10),
            bootstyle="secondary"
        )
        instruction.pack(pady=(0, 15))
        
        # Modern input field
        input_frame = ttk.Frame(input_container)
        input_frame.pack(fill=X, pady=(0, 20))
        
        self.date_entry = ttk.DateEntry(
            input_frame,
            bootstyle="info",
            dateformat="%Y-%m-%d",
            width=20
        )
        self.date_entry.pack(side=LEFT, padx=(0, 15))
        
        # Modern calculate button with hover effect
        self.calc_button = ttk.Button(
            input_frame,
            text="🚀 CALCULATE",
            command=self.calculate_age_threaded,
            bootstyle="success",
            width=15
        )
        self.calc_button.pack(side=LEFT, padx=(0, 10))
        
        # Clear button
        self.clear_button = ttk.Button(
            input_frame,
            text="🔄 RESET",
            command=self.clear_all,
            bootstyle="warning-outline",
            width=12
        )
        self.clear_button.pack(side=LEFT)
        
    def create_results_grid(self):
        """Create modern card-based results grid"""
        results_container = ttk.LabelFrame(
            self.main_container,
            text="📊 Your Time Statistics",
            padding=20,
            bootstyle="info"
        )
        results_container.pack(fill=BOTH, expand=True, pady=(0, 20))
        
        # Main age display - hero section
        hero_frame = ttk.Frame(results_container)
        hero_frame.pack(fill=X, pady=(10, 25))
        
        hero_label = ttk.Label(
            hero_frame,
            text="🎂 YOUR AGE",
            font=('Segoe UI', 12, 'bold'),
            bootstyle="warning"
        )
        hero_label.pack()
        
        self.age_display = ttk.Label(
            hero_frame,
            textvariable=self.age_result,
            style='BigResult.TLabel',
            bootstyle="light"
        )
        self.age_display.pack(pady=(5, 0))
        
        # Stats grid - 2x3 layout
        stats_frame = ttk.Frame(results_container)
        stats_frame.pack(fill=X, pady=(0, 20))
        
        # Row 1
        row1 = ttk.Frame(stats_frame)
        row1.pack(fill=X, pady=(0, 15))
        
        self.create_stat_card(row1, "📅 YEARS", self.years_result, "primary", 0)
        self.create_stat_card(row1, "🗓️ MONTHS", self.months_result, "info", 1)
        self.create_stat_card(row1, "📆 DAYS", self.days_result, "success", 2)
        
        # Row 2
        row2 = ttk.Frame(stats_frame)
        row2.pack(fill=X, pady=(0, 15))
        
        self.create_stat_card(row2, "⏰ HOURS", self.hours_result, "warning", 0)
        self.create_stat_card(row2, "⏱️ MINUTES", self.minutes_result, "danger", 1)
        self.create_stat_card(row2, "🌟 TOTAL DAYS", self.total_days_result, "secondary", 2)
        
    def create_stat_card(self, parent, title, variable, style, column):
        """Create individual stat card with modern styling"""
        card = ttk.LabelFrame(parent, text=title, padding=15, bootstyle=style)
        card.pack(side=LEFT, fill=BOTH, expand=True, padx=5)
        
        value_label = ttk.Label(
            card,
            textvariable=variable,
            style='Result.TLabel',
            bootstyle="light"
        )
        value_label.pack()
        
    def create_additional_info(self):
        """Create additional information section"""
        info_container = ttk.LabelFrame(
            self.main_container,
            text="🔮 Additional Insights",
            padding=20,
            bootstyle="secondary"
        )
        info_container.pack(fill=X, pady=(0, 20))
        
        # Two column layout
        info_grid = ttk.Frame(info_container)
        info_grid.pack(fill=X, pady=10)
        
        # Left column
        left_col = ttk.Frame(info_grid)
        left_col.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        
        ttk.Label(left_col, text="🎉 Next Birthday", font=('Segoe UI', 10, 'bold'), bootstyle="success").pack()
        birthday_label = ttk.Label(left_col, textvariable=self.birthday_result, font=('Segoe UI', 12), bootstyle="light")
        birthday_label.pack(pady=(5, 15))
        
        ttk.Label(left_col, text="⭐ Zodiac Sign", font=('Segoe UI', 10, 'bold'), bootstyle="warning").pack()
        zodiac_label = ttk.Label(left_col, textvariable=self.zodiac_result, font=('Segoe UI', 12), bootstyle="light")
        zodiac_label.pack(pady=(5, 0))
        
        # Right column
        right_col = ttk.Frame(info_grid)
        right_col.pack(side=LEFT, fill=BOTH, expand=True, padx=(10, 0))
        
        ttk.Label(right_col, text="📈 Life Progress", font=('Segoe UI', 10, 'bold'), bootstyle="info").pack()
        
        # Progress bar for life expectancy (assuming 80 years)
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            right_col,
            variable=self.progress_var,
            bootstyle="info-striped",
            length=200
        )
        self.progress_bar.pack(pady=(5, 10))
        
        self.progress_label = ttk.Label(right_col, textvariable=self.progress_text, font=('Segoe UI', 10), bootstyle="secondary")
        self.progress_label.pack()
        
    def create_footer(self):
        """Create modern footer"""
        footer = ttk.Frame(self.main_container)
        footer.pack(fill=X, pady=(10, 0))
        
        separator = ttk.Separator(footer, orient=HORIZONTAL)
        separator.pack(fill=X, pady=(0, 10))
        
        footer_text = ttk.Label(
            footer,
            text="💎 Crafted with modern design principles • Built with ttkbootstrap 💎",
            font=('Segoe UI', 8),
            bootstyle="secondary"
        )
        footer_text.pack()
        
    def setup_animations(self):
        """Setup button animations and effects"""
        self.app.bind('<Return>', lambda e: self.calculate_age_threaded())
        
    def calculate_age_threaded(self):
        """Calculate age in a separate thread for smooth UX"""
        self.calc_button.configure(text="⏳ CALCULATING...", state="disabled")
        thread = threading.Thread(target=self.calculate_age)
        thread.daemon = True
        thread.start()
        
    def calculate_age(self):
        """Enhanced age calculation with comprehensive results"""
        try:
            birth_date = self.date_entry.entry.get()
            if not birth_date:
                messagebox.showwarning("Input Required", "Please select your date of birth.")
                self.reset_button()
                return
                
            birth_dt = datetime.strptime(birth_date, "%Y-%m-%d")
            today = datetime.now()
            
            if birth_dt > today:
                messagebox.showerror("Invalid Date", "Birth date cannot be in the future!")
                self.reset_button()
                return
            
            # Simulate processing time for smooth UX
            time.sleep(0.5)
            
            # Calculate precise age
            age_years = today.year - birth_dt.year
            age_months = today.month - birth_dt.month
            age_days = today.day - birth_dt.day
            
            if age_days < 0:
                age_months -= 1
                if today.month == 1:
                    prev_month_days = 31
                else:
                    prev_month = today.replace(month=today.month-1)
                    next_month = today.replace(day=1)
                    prev_month_days = (next_month - prev_month.replace(day=1)).days
                age_days += prev_month_days
                
            if age_months < 0:
                age_years -= 1
                age_months += 12
            
            # Calculate totals
            total_delta = today - birth_dt
            total_days = total_delta.days
            total_hours = total_days * 24
            total_minutes = total_hours * 60
            total_weeks = total_days // 7
            
            # Next birthday
            next_birthday = datetime(today.year, birth_dt.month, birth_dt.day)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, birth_dt.month, birth_dt.day)
            days_to_birthday = (next_birthday - today).days
            
            # Zodiac sign
            zodiac = self.get_zodiac_sign(birth_dt.month, birth_dt.day)
            
            # Update UI in main thread
            self.app.after(0, lambda: self.update_results(
                age_years, age_months, age_days, total_days, total_hours, 
                total_minutes, total_weeks, days_to_birthday, zodiac
            ))
            
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date.")
            self.reset_button()
    
    def get_zodiac_sign(self, month, day):
        """Calculate zodiac sign based on birth month and day"""
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "♈ Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "♉ Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "♊ Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "♋ Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "♌ Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "♍ Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "♎ Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "♏ Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "♐ Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "♑ Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "♒ Aquarius"
        else:
            return "♓ Pisces"
            
    def update_results(self, years, months, days, total_days, total_hours, 
                      total_minutes, total_weeks, days_to_birthday, zodiac):
        """Update all result displays with animations"""
        # Main age display
        self.age_result.set(f"{years} years, {months} months, {days} days")
        
        # Individual stats
        self.years_result.set(f"{years:,}")
        self.months_result.set(f"{years * 12 + months:,}")
        self.days_result.set(f"{days:,}")
        self.hours_result.set(f"{total_hours:,}")
        self.minutes_result.set(f"{total_minutes:,}")
        self.total_days_result.set(f"{total_days:,}")
        
        # Additional info
        self.birthday_result.set(f"In {days_to_birthday} days")
        self.zodiac_result.set(zodiac)
        
        # Progress bar (assuming 80 years life expectancy)
        progress = min((years / 80) * 100, 100)
        self.progress_var.set(progress)
        self.progress_text.set(f"{progress:.1f}% of 80 years")
        
        # Success animation
        self.calc_button.configure(bootstyle="success", text="✅ CALCULATED!")
        self.app.after(2000, self.reset_button)
        
    def reset_button(self):
        """Reset calculate button to original state"""
        self.calc_button.configure(bootstyle="success", text="🚀 CALCULATE", state="normal")
        
    def clear_all(self):
        """Clear all fields and results"""
        self.date_entry.entry.delete(0, tk.END)
        for var in [self.age_result, self.years_result, self.months_result, 
                   self.days_result, self.hours_result, self.minutes_result,
                   self.total_days_result, self.birthday_result, self.zodiac_result,
                   self.progress_text]:
            var.set("")
        self.progress_var.set(0)
        
    def run(self):
        """Start the application"""
        self.app.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = ModernAgeCalculator()
    app.run()