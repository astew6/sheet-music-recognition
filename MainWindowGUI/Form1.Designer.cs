namespace MainWindowGUI
{
    partial class sheetMusicToMusicXML
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            panel1 = new Panel();
            reviewEditButton = new Button();
            uploadPictureButton = new Button();
            inputPathLabel = new Label();
            panel2 = new Panel();
            analyzeButton = new Button();
            annotateButton = new Button();
            progressIndicatorLabel = new Label();
            analysisProgressBar = new ProgressBar();
            panel3 = new Panel();
            exportMusicXMLButton = new Button();
            outputFileButton = new Button();
            outputPathLabel = new Label();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            panel3.SuspendLayout();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Impact", 30F);
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(429, 48);
            label1.TabIndex = 0;
            label1.Text = "Sheet Music to MusicXML";
            label1.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // panel1
            // 
            panel1.Controls.Add(reviewEditButton);
            panel1.Controls.Add(uploadPictureButton);
            panel1.Controls.Add(inputPathLabel);
            panel1.Location = new Point(12, 60);
            panel1.Name = "panel1";
            panel1.Size = new Size(426, 99);
            panel1.TabIndex = 1;
            // 
            // reviewEditButton
            // 
            reviewEditButton.Font = new Font("Yu Gothic", 15F);
            reviewEditButton.Location = new Point(216, 3);
            reviewEditButton.Name = "reviewEditButton";
            reviewEditButton.Size = new Size(207, 81);
            reviewEditButton.TabIndex = 1;
            reviewEditButton.Text = "Review/Edit";
            reviewEditButton.UseVisualStyleBackColor = true;
            // 
            // uploadPictureButton
            // 
            uploadPictureButton.Font = new Font("Yu Gothic", 15F, FontStyle.Regular, GraphicsUnit.Point, 0);
            uploadPictureButton.Location = new Point(3, 3);
            uploadPictureButton.Name = "uploadPictureButton";
            uploadPictureButton.Size = new Size(207, 81);
            uploadPictureButton.TabIndex = 0;
            uploadPictureButton.Text = "Upload Picture";
            uploadPictureButton.UseVisualStyleBackColor = true;
            // 
            // inputPathLabel
            // 
            inputPathLabel.Font = new Font("Segoe UI", 8F);
            inputPathLabel.Location = new Point(1, 81);
            inputPathLabel.Margin = new Padding(0);
            inputPathLabel.Name = "inputPathLabel";
            inputPathLabel.Size = new Size(420, 17);
            inputPathLabel.TabIndex = 4;
            inputPathLabel.Text = "Input Path:";
            // 
            // panel2
            // 
            panel2.Controls.Add(analyzeButton);
            panel2.Controls.Add(annotateButton);
            panel2.Controls.Add(progressIndicatorLabel);
            panel2.Controls.Add(analysisProgressBar);
            panel2.Location = new Point(12, 165);
            panel2.Name = "panel2";
            panel2.Size = new Size(426, 135);
            panel2.TabIndex = 2;
            // 
            // analyzeButton
            // 
            analyzeButton.Font = new Font("Yu Gothic", 15F);
            analyzeButton.Location = new Point(3, 49);
            analyzeButton.Name = "analyzeButton";
            analyzeButton.Size = new Size(207, 81);
            analyzeButton.TabIndex = 0;
            analyzeButton.Text = "Analyze";
            analyzeButton.UseVisualStyleBackColor = true;
            // 
            // annotateButton
            // 
            annotateButton.Font = new Font("Yu Gothic", 15F);
            annotateButton.Location = new Point(216, 49);
            annotateButton.Name = "annotateButton";
            annotateButton.Size = new Size(207, 81);
            annotateButton.TabIndex = 1;
            annotateButton.Text = "Annotate";
            annotateButton.UseVisualStyleBackColor = true;
            // 
            // progressIndicatorLabel
            // 
            progressIndicatorLabel.Font = new Font("Segoe UI", 8F);
            progressIndicatorLabel.Location = new Point(1, 35);
            progressIndicatorLabel.Margin = new Padding(0);
            progressIndicatorLabel.Name = "progressIndicatorLabel";
            progressIndicatorLabel.Size = new Size(420, 20);
            progressIndicatorLabel.TabIndex = 3;
            progressIndicatorLabel.Text = "Progress";
            progressIndicatorLabel.Click += label2_Click;
            // 
            // analysisProgressBar
            // 
            analysisProgressBar.Location = new Point(3, 3);
            analysisProgressBar.Name = "analysisProgressBar";
            analysisProgressBar.Size = new Size(420, 29);
            analysisProgressBar.TabIndex = 2;
            analysisProgressBar.Value = 46;
            // 
            // panel3
            // 
            panel3.Controls.Add(exportMusicXMLButton);
            panel3.Controls.Add(outputFileButton);
            panel3.Controls.Add(outputPathLabel);
            panel3.Location = new Point(12, 306);
            panel3.Name = "panel3";
            panel3.Size = new Size(426, 99);
            panel3.TabIndex = 5;
            // 
            // exportMusicXMLButton
            // 
            exportMusicXMLButton.Font = new Font("Yu Gothic", 15F);
            exportMusicXMLButton.Location = new Point(216, 3);
            exportMusicXMLButton.Name = "exportMusicXMLButton";
            exportMusicXMLButton.Size = new Size(207, 81);
            exportMusicXMLButton.TabIndex = 1;
            exportMusicXMLButton.Text = "Export MusicXML";
            exportMusicXMLButton.UseVisualStyleBackColor = true;
            // 
            // outputFileButton
            // 
            outputFileButton.Font = new Font("Yu Gothic", 15F, FontStyle.Regular, GraphicsUnit.Point, 0);
            outputFileButton.Location = new Point(3, 3);
            outputFileButton.Name = "outputFileButton";
            outputFileButton.Size = new Size(207, 81);
            outputFileButton.TabIndex = 0;
            outputFileButton.Text = "Output File";
            outputFileButton.UseVisualStyleBackColor = true;
            outputFileButton.Click += button2_Click;
            // 
            // outputPathLabel
            // 
            outputPathLabel.Font = new Font("Segoe UI", 8F);
            outputPathLabel.Location = new Point(1, 81);
            outputPathLabel.Margin = new Padding(0);
            outputPathLabel.Name = "outputPathLabel";
            outputPathLabel.Size = new Size(420, 17);
            outputPathLabel.TabIndex = 4;
            outputPathLabel.Text = "Output Path:";
            // 
            // sheetMusicToMusicXML
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(450, 401);
            Controls.Add(panel3);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Controls.Add(label1);
            Name = "sheetMusicToMusicXML";
            Text = "Sheet Music to MusicXML";
            Load += Form1_Load;
            panel1.ResumeLayout(false);
            panel2.ResumeLayout(false);
            panel3.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Panel panel1;
        private Button reviewEditButton;
        private Button uploadPictureButton;
        private Panel panel2;
        private Button annotateButton;
        private Button analyzeButton;
        private ProgressBar analysisProgressBar;
        private Label progressIndicatorLabel;
        private Label inputPathLabel;
        private Panel panel3;
        private Button exportMusicXMLButton;
        private Button outputFileButton;
        private Label outputPathLabel;
    }
}
