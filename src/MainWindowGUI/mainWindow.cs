using System.Diagnostics;

namespace MainWindowGUI
{
    public partial class sheetMusicToMusicXML : Form
    {
        public string inputPath;
        public string outputPath;
        public imageEditor editor;
        public annotationGui annotator;

        public Image currentImage;

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
            if (inputPath != null)
            {
                using (editor = new imageEditor())
                {
                    editor.ShowDialog();
                    while (editor.DialogResult != DialogResult.OK) { }
                }
            } 
            else
            {
                MessageBox.Show("Please Select an Image path before editing", "invalid image path", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void exportMusicXMLButton_Click(object sender, EventArgs e)
        {

        }

        private void annotateButton_Click(object sender, EventArgs e)
        {
            if (inputPath != null)
            {
                using (annotator = new annotationGui())
                {
                    Process.Start("python", "annotationGui.py");
                    // annotator.ShowDialog();
                    // while (annotator.DialogResult != DialogResult.OK) { }
                }
            } 
            else
            {
                MessageBox.Show("Please Select an Image path and analyze before annotating", "invalid image path", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}
