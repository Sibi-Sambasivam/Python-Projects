package com.pluralsight.courseinfo.cli;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CourseRetriever {
    private static final Logger LOG = LoggerFactory.getLogger(CourseRetriever.class);



    public static void main(String...args) {
        LOG.info("CourseRetriever starting");
        if (args.length == 0){
        LOG.warn("Please provide an author name as first argument");
        return;
        }

        try {
            retrieveCourse(args[0]);
        } catch (Exception e) {
            LOG.error("Unexpected Error");

        }

    }

    private static void retrieveCourse(String authorId) {
        LOG.info("Retrieving courses for author '{}'", authorId);
        CourseRetrievalService courseRetrievalService = new CourseRetrievalService();

        String coursesToStore = courseRetrievalService.getCoursesFor(authorId);
        LOG.info("Retrieved the following courses {}", coursesToStore);
    }


}
