import pytest
import tkinter as tk
from app import ACEestApp


class TestACEestApp:
    """Test cases for ACEest Fitness and Gym Tkinter application"""

    @pytest.fixture
    def app(self):
        """Create app instance for testing"""
        root = tk.Tk()
        root.withdraw()  # Hide the window during testing
        app = ACEestApp(root)
        yield app
        root.destroy()

    def test_app_initialization(self, app):
        """Test that app initializes with correct title and geometry"""
        assert app.root.title() == "ACEest Fitness and Gym"
        assert app.root.geometry() == "1100x750"

    def test_programs_data_structure(self, app):
        """Test that programs data is properly structured"""
        expected_programs = ["Fat Loss (FL)", "Muscle Gain (MG)", "Beginner (BG)"]
        assert list(app.programs.keys()) == expected_programs

        for program in expected_programs:
            assert "workout" in app.programs[program]
            assert "diet" in app.programs[program]
            assert "color" in app.programs[program]

    def test_fat_loss_program_data(self, app):
        """Test Fat Loss program data integrity"""
        fl_data = app.programs["Fat Loss (FL)"]
        assert "Back Squat" in fl_data["workout"]
        assert "Assault Bike" in fl_data["workout"]
        assert "2,000 kcal" in fl_data["diet"]
        assert fl_data["color"] == "#e74c3c"

    def test_muscle_gain_program_data(self, app):
        """Test Muscle Gain program data integrity"""
        mg_data = app.programs["Muscle Gain (MG)"]
        assert "Squat 5x5" in mg_data["workout"]
        assert "Bench 5x5" in mg_data["workout"]
        assert "3,200 kcal" in mg_data["diet"]
        assert mg_data["color"] == "#2ecc71"

    def test_beginner_program_data(self, app):
        """Test Beginner program data integrity"""
        bg_data = app.programs["Beginner (BG)"]
        assert "Circuit Training" in bg_data["workout"]
        assert "Technique Mastery" in bg_data["workout"]
        assert "120g/day" in bg_data["diet"]
        assert bg_data["color"] == "#3498db"

    def test_ui_elements_creation(self, app):
        """Test that all UI elements are created"""
        # Check combobox
        assert app.prog_menu is not None
        assert app.prog_menu["values"] == ("Fat Loss (FL)", "Muscle Gain (MG)", "Beginner (BG)")

        # Check labels
        assert app.work_label is not None
        assert app.diet_label is not None

        # Check initial text
        assert "Select a profile to view workout" in app.work_label["text"]
        assert "Select a profile to view diet" in app.diet_label["text"]

    def test_update_display_fat_loss(self, app):
        """Test display update when Fat Loss is selected"""
        app.prog_var.set("Fat Loss (FL)")
        app.update_display(None)

        assert "Back Squat" in app.work_label["text"]
        assert "2,000 kcal" in app.diet_label["text"]
        assert app.work_label["foreground"] == "#e74c3c"
        assert app.diet_label["foreground"] == "#e74c3c"

    def test_update_display_muscle_gain(self, app):
        """Test display update when Muscle Gain is selected"""
        app.prog_var.set("Muscle Gain (MG)")
        app.update_display(None)

        assert "Squat 5x5" in app.work_label["text"]
        assert "3,200 kcal" in app.diet_label["text"]
        assert app.work_label["foreground"] == "#2ecc71"
        assert app.diet_label["foreground"] == "#2ecc71"

    def test_update_display_beginner(self, app):
        """Test display update when Beginner is selected"""
        app.prog_var.set("Beginner (BG)")
        app.update_display(None)

        assert "Circuit Training" in app.work_label["text"]
        assert "120g/day" in app.diet_label["text"]
        assert app.work_label["foreground"] == "#3498db"
        assert app.diet_label["foreground"] == "#3498db"

    def test_program_selection_binding(self, app):
        """Test that combobox selection triggers update_display"""
        # Simulate selection
        app.prog_menu.set("Fat Loss (FL)")
        app.prog_menu.event_generate("<<ComboboxSelected>>")

        # Check if display was updated
        assert "Back Squat" in app.work_label["text"]

    def test_color_consistency(self, app):
        """Test that colors are consistently applied to both labels"""
        for program, data in app.programs.items():
            app.prog_var.set(program)
            app.update_display(None)

            assert app.work_label["foreground"] == data["color"]
            assert app.diet_label["foreground"] == data["color"]

    def test_workout_content_completeness(self, app):
        """Test that workout plans have sufficient detail"""
        for program, data in app.programs.items():
            workout = data["workout"]
            # Check for common workout indicators
            assert len(workout) > 50  # Reasonable length
            assert any(keyword in workout.upper() for keyword in ["MON", "TUE", "WED", "WORKOUT", "TRAINING"])

    def test_diet_content_completeness(self, app):
        """Test that diet plans have sufficient detail"""
        for program, data in app.programs.items():
            diet = data["diet"]
            # Check for diet indicators
            assert len(diet) > 30  # Reasonable length
            assert any(keyword in diet.upper() for keyword in ["CAL", "PROTEIN", "MEALS", "DIET"])

    def test_ui_layout_structure(self, app):
        """Test that UI has proper hierarchical structure"""
        # Check main frames exist
        assert app.right_panel is not None
        assert app.work_frame is not None
        assert app.diet_frame is not None

        # Check frame titles
        assert "Weekly Workout Chart" in app.work_frame["text"]
        assert "Daily Nutrition Plan" in app.diet_frame["text"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])