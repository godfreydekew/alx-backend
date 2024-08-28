
function createPushNotificationsJobs(jobs,queue ) {
    if (jobs instanceof Array) {
        for (let jobData of jobs) {
            const job = queue.create('push_notification_code_3', jobData)
            .save((err) => {
                if (!err) {
                    console.log(`Notification job created: ${job.id}`);
                } else {
                    console.error('Error creating job:', err);
                }
            });

            job.on('complete', () => {
                console.log(`Notification job ${job.id} completed`);
            });

            job.on('failed', () => {
                console.log(`Notification job ${job.id} failed`);
            });

            job.on('progress', (progress) => {
                console.log(`Notification job ${job.id} ${progress}% complete`);
            });
        }
    } else {
        throw new Error('Jobs is not an array');
    }
}

export default createPushNotificationsJobs;
