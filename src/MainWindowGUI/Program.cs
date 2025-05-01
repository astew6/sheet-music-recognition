namespace MainWindowGUI
{
    internal static class Program
    {
        static public sheetMusicToMusicXML app;
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            ApplicationConfiguration.Initialize();
            app = new sheetMusicToMusicXML();
            Application.Run(app);
        }
    }
}
