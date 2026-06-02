import customtkinter as ctk
from recommender import recommend

# Appearance Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("Movie Recommendation System")
app.geometry("900x650")
app.resizable(False, False)

# Title
title_label = ctk.CTkLabel(
    app,
    text="🎬 Movie Recommendation System",
    font=("Arial", 30, "bold")
)
title_label.pack(pady=20)

# Subtitle
subtitle = ctk.CTkLabel(
    app,
    text="Get Similar Movie Recommendations Instantly",
    font=("Arial", 16)
)
subtitle.pack(pady=5)

# Movie Input
movie_entry = ctk.CTkEntry(
    app,
    width=450,
    height=40,
    placeholder_text="Enter Movie Name (Example: Avatar)"
)
movie_entry.pack(pady=20)

# Recommendation Function
def get_recommendation():

    movie_name = movie_entry.get().strip()

    result_box.delete("1.0", "end")

    if movie_name == "":
        result_box.insert(
            "end",
            "⚠ Please enter a movie name."
        )
        return

    try:
        recommendations = recommend(movie_name)

        result_box.insert(
            "end",
            f"🎥 Recommendations for '{movie_name}'\n\n"
        )

        for movie in recommendations:
            result_box.insert(
                "end",
                f"⭐ {movie}\n"
            )

    except Exception as e:
        result_box.insert(
            "end",
            f"Error:\n{str(e)}"
        )

# Recommend Button
recommend_btn = ctk.CTkButton(
    app,
    text="Recommend Movies",
    width=250,
    height=45,
    command=get_recommendation,
    font=("Arial", 16, "bold")
)
recommend_btn.pack(pady=15)

# Results Label
result_label = ctk.CTkLabel(
    app,
    text="Recommended Movies",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=10)

# Result Box
result_box = ctk.CTkTextbox(
    app,
    width=700,
    height=300,
    font=("Arial", 15)
)
result_box.pack(pady=10)

# Footer
footer = ctk.CTkLabel(
    app,
    text="Built with Python • Scikit-Learn • CustomTkinter",
    font=("Arial", 12)
)
footer.pack(side="bottom", pady=10)

# Run Application
app.mainloop()