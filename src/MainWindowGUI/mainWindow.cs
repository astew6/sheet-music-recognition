namespace MainWindowGUI
{
    public partial class sheetMusicToMusicXML : Form
    {
        public string inputPath;
        public string outputPath;
        public sheetMusicToMusicXML()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK) //opens the file dialog until it is dismissed
            {
                outputPath = saveFileDialog1.FileName;
                outputPathLabel.Text = $"Output Path: {outputPath}"; //sets the output file label to the path selected in the file dialog
            }
        }

        private void uploadPictureButton_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK) //opens the file dialog until it is dismissed
            {
                inputPath = openFileDialog1.FileName; //sets the input file directory variable to the path selected in the file dialog
                inputPathLabel.Text = $"Input Path: {inputPath}"; //sets the input file label to the path selected in the file dialog
            }
        }

        private void reviewEditButton_Click(object sender, EventArgs e)
        {
            using (var editor = new imageEditor())
            {
                editor.ShowDialog();
                while (editor.DialogResult != DialogResult.OK) { }
            }
        }

        private void exportMusicXMLButton_Click(object sender, EventArgs e)
        {

        }
    }
}
