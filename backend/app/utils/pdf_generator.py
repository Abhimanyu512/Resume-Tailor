from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from io import BytesIO
from typing import Dict, List, Any
import os

class ResumePDFGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the resume"""
        # Header style
        self.styles.add(ParagraphStyle(
            name='Header',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#2E5BBA'),
            alignment=TA_CENTER
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.HexColor('#2E5BBA'),
            borderWidth=1,
            borderColor=colors.HexColor('#2E5BBA'),
            borderPadding=5,
            leftIndent=0
        ))
        
        # Job title style
        self.styles.add(ParagraphStyle(
            name='JobTitle',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=6,
            textColor=colors.HexColor('#2E5BBA'),
            fontName='Helvetica-Bold'
        ))
        
        # Company style
        self.styles.add(ParagraphStyle(
            name='Company',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            fontName='Helvetica-Bold'
        ))
        
        # Duration style
        self.styles.add(ParagraphStyle(
            name='Duration',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            fontName='Helvetica-Oblique',
            textColor=colors.grey
        ))
        
        # Description style
        self.styles.add(ParagraphStyle(
            name='Description',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=12,
            leftIndent=20,
            alignment=TA_JUSTIFY
        ))
        
        # Skills style
        self.styles.add(ParagraphStyle(
            name='Skills',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=6,
            leftIndent=20
        ))
        
        # Project title style
        self.styles.add(ParagraphStyle(
            name='ProjectTitle',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            fontName='Helvetica-Bold',
            textColor=colors.HexColor('#2E5BBA')
        ))
        
        # Tech stack style
        self.styles.add(ParagraphStyle(
            name='TechStack',
            parent=self.styles['Normal'],
            fontSize=9,
            spaceAfter=8,
            fontName='Helvetica-Oblique',
            textColor=colors.grey
        ))

    def generate_pdf(self, resume_data: Dict[str, Any]) -> BytesIO:
        """Generate a PDF from the resume data"""
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
        
        story = []
        
        # Header with name
        story.append(Paragraph(resume_data.get('name', 'Resume'), self.styles['Header']))
        story.append(Spacer(1, 20))
        
        # Summary
        if resume_data.get('summary'):
            story.append(Paragraph('PROFESSIONAL SUMMARY', self.styles['SectionHeader']))
            story.append(Paragraph(resume_data['summary'], self.styles['Description']))
        
        # Skills
        if resume_data.get('skills'):
            story.append(Paragraph('TECHNICAL SKILLS', self.styles['SectionHeader']))
            skills_text = ', '.join(resume_data['skills'])
            story.append(Paragraph(skills_text, self.styles['Skills']))
        
        # Experience
        if resume_data.get('experience'):
            story.append(Paragraph('PROFESSIONAL EXPERIENCE', self.styles['SectionHeader']))
            
            for exp in resume_data['experience']:
                # Job title and company
                job_info = f"{exp.get('job_title', '')} at {exp.get('company', '')}"
                story.append(Paragraph(job_info, self.styles['JobTitle']))
                
                # Duration
                if exp.get('duration'):
                    story.append(Paragraph(exp['duration'], self.styles['Duration']))
                
                # Description
                if exp.get('description'):
                    story.append(Paragraph(exp['description'], self.styles['Description']))
                
                story.append(Spacer(1, 12))
        
        # Projects
        if resume_data.get('projects'):
            story.append(Paragraph('PROJECTS', self.styles['SectionHeader']))
            
            for project in resume_data['projects']:
                if project.get('title'):
                    story.append(Paragraph(project['title'], self.styles['ProjectTitle']))
                
                if project.get('description'):
                    story.append(Paragraph(project['description'], self.styles['Description']))
                
                if project.get('tech_stack'):
                    tech_text = f"Technologies: {', '.join(project['tech_stack'])}"
                    story.append(Paragraph(tech_text, self.styles['TechStack']))
                
                story.append(Spacer(1, 12))
        
        # Education
        if resume_data.get('education'):
            story.append(Paragraph('EDUCATION', self.styles['SectionHeader']))
            
            for edu in resume_data['education']:
                if edu.get('degree') and edu.get('institution'):
                    edu_info = f"{edu['degree']} - {edu['institution']}"
                    story.append(Paragraph(edu_info, self.styles['JobTitle']))
                    
                    if edu.get('duration'):
                        story.append(Paragraph(edu['duration'], self.styles['Duration']))
                    
                    story.append(Spacer(1, 12))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer

def generate_resume_pdf(resume_data: Dict[str, Any]) -> BytesIO:
    """Convenience function to generate PDF from resume data"""
    generator = ResumePDFGenerator()
    return generator.generate_pdf(resume_data) 