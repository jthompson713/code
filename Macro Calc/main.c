#include <gtk/gtk.h>
#include <stdio.h>

typedef struct {
    GtkEntry *name_entry;        // Changed from GtkWidget
    GtkEntry *calories_entry;
    GtkEntry *protein_entry;
    GtkEntry *fats_entry;
    GtkEntry *carbs_entry;
    GtkEntry *servings_entry;
    GtkLabel *result_label;      // Changed from GtkWidget
} AppWidgets;

static void calculate_macros(GtkButton *button, gpointer user_data) {
    AppWidgets *widgets = (AppWidgets *)user_data;
    
    // Get values from entries using correct GTK4 API
    const char *name = gtk_editable_get_text(GTK_EDITABLE(widgets->name_entry));
    float calories = atof(gtk_editable_get_text(GTK_EDITABLE(widgets->calories_entry)));
    float protein = atof(gtk_editable_get_text(GTK_EDITABLE(widgets->protein_entry)));
    float fats = atof(gtk_editable_get_text(GTK_EDITABLE(widgets->fats_entry)));
    float carbs = atof(gtk_editable_get_text(GTK_EDITABLE(widgets->carbs_entry)));
    int servings = atoi(gtk_editable_get_text(GTK_EDITABLE(widgets->servings_entry)));

    if (servings <= 0) {
        gtk_label_set_text(widgets->result_label, "Please enter valid servings");
        return;
    }

    char result[512];
    snprintf(result, sizeof(result),
             "Recipe: %s\n"
             "Per Serving (%d servings total):\n"
             "Calories: %.1f\n"
             "Protein: %.1f g\n"
             "Fats: %.1f g\n"
             "Carbs: %.1f g",
             name, servings,
             calories/servings,
             protein/servings,
             fats/servings,
             carbs/servings);
    
    gtk_label_set_text(widgets->result_label, result);
}

static void button_clicked(GtkWidget *widget, gpointer data) {
    g_print("Button clicked!\n");
}

static void activate(GtkApplication *app, gpointer user_data) {
    AppWidgets *widgets = g_new(AppWidgets, 1);
    
    // Window setup
    GtkWidget *window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "Recipe Macro Calculator");
    gtk_window_set_default_size(GTK_WINDOW(window), 400, 500);
    
    // Grid setup with spacing and margins
    GtkGrid *grid = GTK_GRID(gtk_grid_new());
    gtk_grid_set_row_spacing(grid, 10);
    gtk_grid_set_column_spacing(grid, 10);
    gtk_widget_set_margin_start(GTK_WIDGET(grid), 20);
    gtk_widget_set_margin_end(GTK_WIDGET(grid), 20);
    gtk_widget_set_margin_top(GTK_WIDGET(grid), 20);
    gtk_widget_set_margin_bottom(GTK_WIDGET(grid), 20);
    
    // Create labels
    GtkWidget *name_label = gtk_label_new("Recipe Name:");
    GtkWidget *calories_label = gtk_label_new("Total Calories:");
    GtkWidget *protein_label = gtk_label_new("Total Protein (g):");
    GtkWidget *fats_label = gtk_label_new("Total Fats (g):");
    GtkWidget *carbs_label = gtk_label_new("Total Carbs (g):");
    GtkWidget *servings_label = gtk_label_new("Number of Servings:");
    
    // Create entries
    widgets->name_entry = GTK_ENTRY(gtk_entry_new());
    widgets->calories_entry = GTK_ENTRY(gtk_entry_new());
    widgets->protein_entry = GTK_ENTRY(gtk_entry_new());
    widgets->fats_entry = GTK_ENTRY(gtk_entry_new());
    widgets->carbs_entry = GTK_ENTRY(gtk_entry_new());
    widgets->servings_entry = GTK_ENTRY(gtk_entry_new());
    
    // Make entries expand horizontally
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->name_entry), TRUE);
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->calories_entry), TRUE);
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->protein_entry), TRUE);
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->fats_entry), TRUE);
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->carbs_entry), TRUE);
    gtk_widget_set_hexpand(GTK_WIDGET(widgets->servings_entry), TRUE);
    
    // Attach labels and entries to grid
    gtk_grid_attach(grid, name_label, 0, 0, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->name_entry), 1, 0, 1, 1);
    
    gtk_grid_attach(grid, calories_label, 0, 1, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->calories_entry), 1, 1, 1, 1);
    
    gtk_grid_attach(grid, protein_label, 0, 2, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->protein_entry), 1, 2, 1, 1);
    
    gtk_grid_attach(grid, fats_label, 0, 3, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->fats_entry), 1, 3, 1, 1);
    
    gtk_grid_attach(grid, carbs_label, 0, 4, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->carbs_entry), 1, 4, 1, 1);
    
    gtk_grid_attach(grid, servings_label, 0, 5, 1, 1);
    gtk_grid_attach(grid, GTK_WIDGET(widgets->servings_entry), 1, 5, 1, 1);
    
    // Create and attach button
    GtkButton *calculate_button = GTK_BUTTON(gtk_button_new_with_label("Calculate"));
    gtk_widget_set_hexpand(GTK_WIDGET(calculate_button), TRUE);
    gtk_grid_attach(grid, GTK_WIDGET(calculate_button), 0, 6, 2, 1);
    
    // Create and attach result label
    widgets->result_label = GTK_LABEL(gtk_label_new(""));

    gtk_grid_attach(grid, GTK_WIDGET(widgets->result_label), 0, 7, 2, 1);
    
    // Connect button signal
    g_signal_connect(calculate_button, "clicked", G_CALLBACK(calculate_macros), widgets);
    
    // Set window child and show
    gtk_window_set_child(GTK_WINDOW(window), GTK_WIDGET(grid));
    gtk_window_present(GTK_WINDOW(window));
}

int main(int argc, char **argv) {
    GtkApplication *app = gtk_application_new("org.gtk.example", G_APPLICATION_DEFAULT_FLAGS);
    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
    int status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);
    return status;
}