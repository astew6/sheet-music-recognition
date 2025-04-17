namespace MainWindowGUI
{
    public partial class sheetMusicToMusicXML : Form
    {
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
                outputPathLabel.Text = saveFileDialog1.FileName; //sets the output file label to the path selected in the file dialog
            }
        }

        private void uploadPictureButton_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK) //opens the file dialog until it is dismissed
            {
                inputPathLabel.Text = openFileDialog1.FileName; //sets the input file label to the path selected in the file dialog
            }
        }

        private void reviewEditButton_Click(object sender, EventArgs e)
        {
            using (var editor = new imageEditor())
            {
                editor.ShowDialog();
                while (editor.DialogResult != DialogResult.OK)
                {
                }
            }
        }

        private void exportMusicXMLButton_Click(object sender, EventArgs e)
        {

        }
    }
}
